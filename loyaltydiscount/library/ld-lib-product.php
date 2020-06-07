<?php

$getParam = isset($_REQUEST['param'])?$_REQUEST['param']:'';

if(!empty($getParam)){
  if($getParam=='post_product_form_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $query="SELECT pid FROM wp_ld_producr_discount WHERE pid = ".$_REQUEST['pid'];
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );
    $str='N';
    if(sizeof($data)==0){
      $table = 'wp_ld_producr_discount';
      $data=array(
        "pid" =>$_REQUEST['pid'],
        "0" =>$_REQUEST['disL'],
        "1" =>$_REQUEST['disM'],
        "2" =>$_REQUEST['disH']
      );
      $wpdb->insert($table,$data);
      $str='Y';
    }
    echo $str;
    die;
  }
  if($getParam=='get_product_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $query="SELECT * FROM wp_ld_producr_discount";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );

    $str=json_encode($data);
    echo $str;
    die;
  }
  if ($getParam=='get_product_form_data_of') {
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $query="SELECT * FROM wp_ld_producr_discount WHERE pid =".$_REQUEST['Upid'];
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );

    $str=json_encode($data);
    echo $str;
    die;
  }
  if ($getParam=='update_product_form_data') {
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $table = 'wp_ld_producr_discount';
    $data = array(
      '0' =>$_REQUEST['UdisL'],
      '1'=>$_REQUEST['UdisM'],
      '2'=>$_REQUEST['UdisH']
    );
    $where = array(
      'pid' =>$_REQUEST['Upid']
    );
    $updated = $wpdb->update( $table, $data, $where );
    if ( false === $updated ) {
        echo 'N';
    } else {
        echo 'Y';
    }
    die;
  }
  if ($getParam=='delete_product_form_data') {
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $table = 'wp_ld_producr_discount';
    $where = array(
      'pid' =>$_REQUEST['Dpid']
    );
    $deleted = $wpdb->delete( $table, $where );
    if ( false === $deleted ) {
        echo 'N';
    } else {
        echo 'Y';
    }
    die;
  }
}
