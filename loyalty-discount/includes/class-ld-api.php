<?php

class ld_api extends WP_REST_Controller {
  public function register_routes() {
        $namespace = 'ld/v1';

        register_rest_route( $namespace, '/posts/(?P<id>[a-zA-Z0-9\ ]+)', [
              array(
                'methods'             => 'POST',
                'callback'            => array( $this, 'get_items' ),
                'permission_callback' => array( $this, 'get_items_security_check' )
              )
        ]);
        register_rest_route( $namespace, '/discount/(?P<pid>\d+)', [
              array(
                'methods'             => 'POST',
                'callback'            => array( $this, 'get_discount' ),
                'permission_callback' => array( $this, 'get_items_security_check' )
              )
        ]);
        register_rest_route( $namespace, '/code/(?P<id>[a-zA-Z0-9\ ]+)', [
              array(
                'methods'             => 'POST',
                'callback'            => array( $this, 'get_code' ),
                'permission_callback' => array( $this, 'get_items_security_check' )
              )
        ]);
    }

    public function get_items_security_check($request) {
      global $wpdb;
    	require_once(ABSPATH."wp-admin/includes/upgrade.php");
      $query="SELECT security_key FROM wp_ld_api_keys WHERE security_key = '".$request->get_header('SecurityKey')."'";
      $dbresult=$wpdb->get_results(
        $wpdb->prepare(
              $query,''
          )
      );
      if (count($dbresult)==0){
        return false;
      }
      return true;
    }

    public function get_items($request) {
      global $wpdb;
    	require_once(ABSPATH."wp-admin/includes/upgrade.php");
      $query="SELECT * FROM wp_loyaltydiscount WHERE customer_id = ".$request['id']." AND product_id = ".$request['pid']." AND LD_aquire = 'No'";
      $data=$wpdb->get_results(
        $wpdb->prepare(
              $query,''
          )
      );
      return $data;
    }
    public function get_discount($request){
        global $wpdb;
        require_once(ABSPATH."wp-admin/includes/upgrade.php");
        $query="SELECT * FROM wp_ld_producr_discount WHERE pid = ".$request['pid'];
        $data=$wpdb->get_results(
          $wpdb->prepare(
                $query,''
            )
        );
        return $data;
    }
    public function get_code($request) {
      global $wpdb;
    	require_once(ABSPATH."wp-admin/includes/upgrade.php");
      $query="SELECT lastOfferCode FROM wp_loyaltydiscount WHERE id = (SELECT MAX(id) FROM wp_loyaltydiscount WHERE customer_id = ".$request['id']." AND product_id = ".$request['pid']." AND LD_aquire = 'Yes')";
      $data=$wpdb->get_results(
        $wpdb->prepare(
              $query,''
          )
      );
      return $data;
    }
}
