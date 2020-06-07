<?php

$getParam = isset($_REQUEST['param'])?$_REQUEST['param']:'';

if(!empty($getParam)){
  if($getParam=='get_dashboad_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $query="SELECT COUNT(DISTINCT order_id) as cord, SUM(discount) as dis,SUM(price) as price FROM wp_loyaltydiscount";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );
    //$data=array_merge($data,$data1);
    $str=json_encode($data);
    echo $str;
    die;
  }
  if($getParam=='get_product_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $query="SELECT pid FROM wp_ld_producr_discount";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );
    //$data=array_merge($data,$data1);
    $str=json_encode($data);
    echo $str;
    die;
  }
  if($getParam=='get_product_form_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $result=array();
    $query="SELECT YEAR(date_time) as year,MONTH(date_time) as month,DAY(date_time) as date,COUNT(lastOfferCode)as L FROM wp_loyaltydiscount WHERE MONTH(CURRENT_DATE)>=MONTH(date_time) AND product_id=".$_REQUEST['pld_menu']." AND MOD(lastOfferCode,10) > 0 AND discount>0 GROUP BY DATE(date_time)";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );
    $result=array_merge($result,$data);
    $query="SELECT YEAR(date_time) as year,MONTH(date_time) as month,DAY(date_time) as date,COUNT(lastOfferCode)as M FROM wp_loyaltydiscount WHERE MONTH(CURRENT_DATE)>=MONTH(date_time) AND product_id=".$_REQUEST['pld_menu']." AND MOD((ROUND(lastOfferCode/10)),10) > 0 AND discount>0 GROUP BY DATE(date_time)";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );
    $result=array_merge($result,$data);
    $query="SELECT YEAR(date_time) as year,MONTH(date_time) as month,DAY(date_time) as date,COUNT(lastOfferCode)as H FROM wp_loyaltydiscount WHERE MONTH(CURRENT_DATE)>=MONTH(date_time) AND product_id=".$_REQUEST['pld_menu']." AND MOD((ROUND(lastOfferCode/100)),10) > 0 AND discount>0 GROUP BY DATE(date_time)";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );
    $result=array_merge($result,$data);
    //$data=array_merge($data,$data1);
    $str=json_encode($result);
    echo $str;
    //print_r($_REQUEST['pld_menu']);
    die;
  }
  if($getParam=='get_dashboad_chart_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $query="SELECT YEAR(date_time) as year,MONTH(date_time) as month,DAY(date_time) as date,SUM(price) as price,SUM(discount) as discount, COUNT(order_id) as ord FROM wp_loyaltydiscount WHERE MONTH(CURRENT_DATE)>=MONTH(date_time) GROUP BY DATE(date_time)";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );
    //$data=array_merge($data,$data1);
    $str=json_encode($data);
    echo $str;
    die;
  }
}
