<?php

function loyaltydiscount_table_delete(){
  global $wpdb;

  if(is_null($wpdb->get_var("SHOW TABLES LIKE 'wp_loyaltydiscount'"))!=1){
      $wpdb->query("DROP TABLE IF EXISTS wp_loyaltydiscount");
  }
  if(is_null($wpdb->get_var("SHOW TABLES LIKE 'wp_ld_api_keys'"))!=1){
      $wpdb->query("DROP TABLE IF EXISTS wp_ld_api_keys");
  }
}

?>
