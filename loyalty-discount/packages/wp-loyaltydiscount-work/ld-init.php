<?php

function add_my_custom_menu()
{
  add_menu_page("loyaltydiscount","Loyalty Discount","manage_options","loyalty-discount","plugin_dashboard_view","dashicons-dashboard",6);
  add_submenu_page("loyalty-discount","dashboard","Dashboard","manage_options","loyalty-discount","plugin_dashboard_view");
  add_submenu_page("loyalty-discount","product","Product Settings","manage_options","product","plugin_product_view");
  add_submenu_page("loyalty-discount","api","API Settings","manage_options","api","plugin_api_view");
  add_submenu_page("loyalty-discount","general","General Settings","manage_options","general","plugin_general_view");
}

function plugin_dashboard_view()
{
  include_once(PLUGIN_DIR_PATH."/views/dashboard.php");
}

function plugin_product_view()
{
  include_once(PLUGIN_DIR_PATH."/views/product.php");
}

function plugin_api_view()
{
  include_once(PLUGIN_DIR_PATH."/views/api.php");
}

function plugin_general_view()
{
  include_once(PLUGIN_DIR_PATH."/views/general.php");
}

add_action("admin_menu","add_my_custom_menu");


?>
