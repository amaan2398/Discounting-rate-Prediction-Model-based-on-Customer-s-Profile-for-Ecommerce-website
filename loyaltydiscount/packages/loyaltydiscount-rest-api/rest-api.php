<?php

  include_once(PLUGIN_DIR_PATH.'/includes/class-ld-api.php');

  add_action('rest_api_init', function () {
    $ld_api = new ld_api();
    $ld_api->register_routes();
  });


?>
