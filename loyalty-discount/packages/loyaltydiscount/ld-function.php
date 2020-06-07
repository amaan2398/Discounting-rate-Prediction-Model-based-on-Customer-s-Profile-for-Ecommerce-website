<?php


function api_call($cust_id,$pid){
  $arrjs=array("id"=>$cust_id,"product_c"=>$pid);
  $send_json=json_encode($arrjs);
  $url="127.0.0.1:5000/discount_model";
  $ch= curl_init($url);
  curl_setopt($ch,CURLOPT_POSTFIELDS,$send_json);
  curl_setopt($ch,CURLOPT_HTTPHEADER,array('Content-Type:application/json'));
  curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
  $result =(array) json_decode(curl_exec($ch));
  curl_close($ch);
  return $result;
}

add_action( 'woocommerce_before_calculate_totals', 'add_custom_price', 10, 1);

function add_custom_price( $cart_object ) {
    $user=wp_get_current_user();
    $cust_id = $user->ID;
    global $woocommerce;
    global $ld;
    $ld->prodDiscount = array('id' => $cust_id);
    $ld->t=0;
    if ( is_admin() && ! defined( 'DOING_AJAX' ) )
        return;

    if ( did_action( 'woocommerce_before_calculate_totals' ) >= 2 )
        return;

    foreach ( $cart_object->get_cart() as $cart_item ) {
        $pid = $cart_item['data']->get_id();
        $result=api_call($cust_id,$pid);
        $discount=$result['response'];
        $ld->t+=$discount;
        ## Price calculation ##
        //print_r($cart_item['data']->price);
        global $wpdb;
        require_once(ABSPATH."wp-admin/includes/upgrade.php");
        $query="SELECT status FROM wp_ld_tax_status";
        $database=$wpdb->get_results(
          $wpdb->prepare(
                $query,''
            )
        );
        if (((array)$database[0])['status'] == 1){
          if($ttax>0){
            $price = $cart_item['data']->price - (($discount/$cart_item['quantity'])/0.2);
          }
          else{
            $price = $cart_item['data']->price - ($discount/$cart_item['quantity']);
          }
        }
        else {
          $price = $cart_item['data']->price - ($discount/$cart_item['quantity']);
        }
        array_push($ld->prodDiscount,array('pid'=>$pid,'price'=>$price*$cart_item['quantity']
                    ,'discount'=>$discount,'code'=>$result['code']));
        ## Set the price with WooCommerce compatibility ##
        if ( version_compare( WC_VERSION, '3.0', '<' ) ) {
            $cart_item['data']->price = $price; // Before WC 3.0
        } else {
            $cart_item['data']->set_price( $price ); // WC 3.0+
        }
    }
}



function discount_view() {

    global $woocommerce;
    global $ld;
    $discount_total = $ld->t;

    if ( $discount_total > 0 ) {
    echo '<tr class="cart-discount">
    <th>'. __( 'Your Loyalty Discount', 'woocommerce' ) .'</th>
    <td data-title=" '. __( 'Your Loyalty Discount', 'woocommerce' ) .' ">'
    . wc_price( $discount_total + $woocommerce->cart->discount_cart ) .'</td>
    </tr>';
    }

}

// Hook our values to the Basket and Checkout pages

add_action( 'woocommerce_cart_totals_after_order_total', 'discount_view', 99);
add_action( 'woocommerce_review_order_after_order_total', 'discount_view', 99);


add_action('woocommerce_checkout_order_processed','placed_order_update_database', 10, 1);
function placed_order_update_database($order_id){
  global $wpdb;
  require_once(ABSPATH."wp-admin/includes/upgrade.php");
  global $ld;
  $i=0;
  for($i=0;$i<sizeof($ld->prodDiscount)-1;$i++){
      $table = $wpdb->prefix.'loyaltydiscount';
      $data=array(
            "customer_id" =>$ld->prodDiscount["id"],
            "product_id" => $ld->prodDiscount[$i]["pid"],
            "order_id" => $order_id,
            "price" =>$ld->prodDiscount[$i]["price"],
            "lastOfferCode" => $ld->prodDiscount[$i]["code"],
            "discount" => $ld->prodDiscount[$i]["discount"],
            "LD_aquire" => ($ld->prodDiscount[$i]["discount"] > 0 ? "Yes" : "No")
          );
      if ($data["LD_aquire"]=="Yes"){
          $upData=array("LD_aquire"=>$data["LD_aquire"]);
          $where=array("customer_id" =>$data["customer_id"],
                      "product_id" => $data["product_id"]);
          $wpdb->update(
            $table,
            $upData,
            $where
          );
      }
      $wpdb->insert($table,$data);
  }
}

?>
