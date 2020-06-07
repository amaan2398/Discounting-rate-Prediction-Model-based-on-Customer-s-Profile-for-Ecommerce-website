<?php

function loyaltydiscount_table(){
  global $wpdb;
  require_once(ABSPATH."wp-admin/includes/upgrade.php");

  if(is_null($wpdb->get_var("SHOW TABLES LIKE 'wp_loyaltydiscount'"))==1){
    $sql_query_to_create_table =   "CREATE TABLE `wp_loyaltydiscount` (
                                     `id` bigint(20) NOT NULL AUTO_INCREMENT,
                                     `customer_id` bigint(20) NOT NULL,
                                     `product_id` bigint(20) NOT NULL,
                                     `order_id` bigint(20) NOT NULL,
                                     `date_time` datetime NOT NULL DEFAULT current_timestamp(),
                                     `price` float NOT NULL,
                                     `lastOfferCode` bigint(20) NOT NULL,
                                     `discount` float NOT NULL DEFAULT 0,
                                     `LD_aquire` text NOT NULL DEFAULT 'No',
                                     PRIMARY KEY (`id`)
                                    ) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4";
    dbDelta($sql_query_to_create_table);
  }
  if(is_null($wpdb->get_var("SHOW TABLES LIKE 'wp_ld_api_keys'"))==1){
    $sql_query_to_create_table = "CREATE TABLE `wp_ld_api_keys` (
                                   `key_id` bigint(20) NOT NULL AUTO_INCREMENT,
                                   `description` varchar(200) NOT NULL,
                                   `security_key` varchar(64) NOT NULL,
                                   `last_access` datetime NOT NULL DEFAULT current_timestamp(),
                                   PRIMARY KEY (`key_id`),
                                   UNIQUE KEY `security_key` (`security_key`)
                                  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";
    dbDelta($sql_query_to_create_table);
  }
  if(is_null($wpdb->get_var("SHOW TABLES LIKE 'wp_ld_producr_discount'"))==1){
    $sql_query_to_create_table = "CREATE TABLE `wp_ld_producr_discount` (
                                   `pid` bigint(20) NOT NULL,
                                   `0` float NOT NULL,
                                   `1` float NOT NULL,
                                   `2` float NOT NULL,
                                   UNIQUE KEY `pid` (`pid`)
                                  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";
    dbDelta($sql_query_to_create_table);
  }
  if(is_null($wpdb->get_var("SHOW TABLES LIKE 'wp_ld_tax_status'"))==1){
    $sql_query_to_create_table = "CREATE TABLE `wp_ld_tax_status` (
                                   `status` int(11) NOT NULL DEFAULT 0
                                  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";
    dbDelta($sql_query_to_create_table);
  }

}


?>
