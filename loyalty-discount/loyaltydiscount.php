<?php
  /*
  Plugin Name: Loyalty Discount
  Description: This is an plugin which will give discount to customer based on customer loyalty score by the use of ML/AI supervise model.
  Version:0.1
  Author: Amaan Shaikh
  Author URI:www.linkedin.com/in/amaan-shaikh-a91735178
  */
  if (!defined('ABSPATH')) {
      exit;
  }

  define("PLUGIN_DIR_PATH",plugin_dir_path(__FILE__));
  define("PLUGIN_URL",plugins_url());
  define("PLUGIN_VERSION","0.1");
  include_once(PLUGIN_DIR_PATH."/includes/class-loyalty-discount.php");
  global $ld;
  $ld =new loyaltydiscount(array(),0);
  include_once(PLUGIN_DIR_PATH."/packages/loyaltydiscount-rest-api/rest-api.php");

  include_once(PLUGIN_DIR_PATH."/packages/wp-loyaltydiscount-work/ld-init.php");



  include_once(PLUGIN_DIR_PATH."/packages/loyaltydiscount/ld-database-init.php");
  register_activation_hook(__FILE__,"loyaltydiscount_table");

  include_once(PLUGIN_DIR_PATH."/packages/loyaltydiscount/ld-assets-load.php");

  include(PLUGIN_DIR_PATH."/packages/loyaltydiscount/ld-function.php");

  include_once('uninstall.php');
  register_uninstall_hook(__FILE__,"loyaltydiscount_table_delete");
?>
