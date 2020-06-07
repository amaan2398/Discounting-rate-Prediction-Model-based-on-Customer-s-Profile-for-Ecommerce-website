<?php

function plugin_assets(){
    wp_enqueue_style("style_css",PLUGIN_URL."/loyalty-discount/assets/css/style.css","",PLUGIN_VERSION);
    wp_enqueue_script("plugin_script",PLUGIN_URL."/loyalty-discount/assets/js/script.js","",PLUGIN_VERSION,true);
    wp_localize_script("plugin_script","ajax_url",admin_url("admin-ajax.php"));
}
add_action("init","plugin_assets");

if(isset($_REQUEST['action'])){
  switch ($_REQUEST['action']) {
    case 'loyalty-discount-lib_api':
      add_action("admin_init","add_ld_lib_api");
      function add_ld_lib_api(){
        global $wpdb;
        include_once PLUGIN_DIR_PATH."/library/ld-lib-api.php";
      }
      break;
    case 'loyalty-discount-lib_dashboard':
      add_action("admin_init","add_ld_lib_dashboad");
      function add_ld_lib_dashboad(){
        global $wpdb;
        include_once PLUGIN_DIR_PATH."/library/ld-lib-dashboard.php";
      }
      break;
    case 'loyalty-discount-lib_product':
      add_action("admin_init","add_ld_lib_product");
      function add_ld_lib_product(){
        global $wpdb;
        include_once PLUGIN_DIR_PATH."/library/ld-lib-product.php";
      }
      break;
    case 'loyalty-discount-lib_general':
      add_action("admin_init","add_ld_lib_general");
      function add_ld_lib_general(){
        global $wpdb;
        include_once PLUGIN_DIR_PATH."/library/ld-lib-general.php";
      }
      break;
  }

}

?>
