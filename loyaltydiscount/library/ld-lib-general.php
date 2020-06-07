<?php

$getParam = isset($_REQUEST['param'])?$_REQUEST['param']:'';

if(!empty($getParam)){
  if($getParam=='post_general_form_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");

    $table = 'wp_ld_tax_status';
    $r=$_REQUEST['tax_toggle']=='on'?1:0;
    $data=array(
      "status" =>$r
    );
    $where=array(
      "id"=>1
    );
    $updated = $wpdb->update( $table, $data, $where );
    if ( false === $updated ) {
        echo 'N';
    } else {
        echo 'Y';
    }
    //echo $r;
    die;
  }
}
