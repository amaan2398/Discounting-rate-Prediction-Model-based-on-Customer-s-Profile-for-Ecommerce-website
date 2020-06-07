<?php

$getParam = isset($_REQUEST['param'])?$_REQUEST['param']:'';

if(!empty($getParam)){
  if($getParam=='post_api_form_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $table = 'wp_ld_api_keys';
    $str = substr(base64_encode(sha1(mt_rand())), 0, 32);
    $data=array(
          "description" =>$_REQUEST['description'],
          "security_key" =>$str
        );
    $wpdb->insert($table,$data);
    echo $str;
    die;
  }
  if($getParam=='post_api_delete_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $table = 'wp_ld_api_keys';
    $where = array(
      "key_id"=>$_REQUEST['api_id']
    );
    $updated = $wpdb->delete($table,$where);
    if ( false === $updated ) {
        echo 'N';
    } else {
        echo 'Y';
    }
    die;
  }

  if($getParam=='get_api_key_data'){
    global $wpdb;
    require_once(ABSPATH."wp-admin/includes/upgrade.php");
    $query="SELECT * FROM wp_ld_api_keys";
    $data=$wpdb->get_results(
      $wpdb->prepare(
            $query,''
        )
    );

    $str=json_encode($data);
    echo $str;
    die;
  }

}
