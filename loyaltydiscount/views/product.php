<?php  ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
    <style>
      label.error{
        color: red;
      }
      .scrollable{
        width: 100%;
        height: 300px;
        overflow-y: scroll;
      }
      .btn{
        margin-bottom: 10px;
      }
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.16.0/jquery.validate.min.js"></script>
    <!--<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/dt-1.10.20/datatables.min.css"/>-->
    <script>
        $(function(){
          $.fn.table_refresher=function(){
            var post_data = "&action=loyalty-discount-lib_product&param=get_product_data";
            $.post(ajax_url,post_data,function(response){
                //console.log(response);
                var obj = JSON.parse(response);
                var i =0;
                var str='';
                if(obj.length>8){
                  $('#ld_pro_table_size').addClass('scrollable');
                }
                else{
                  $('#ld_pro_table_size').removeClass('scrollable');
                }
                for(i=0;i<obj.length;i++){
                  str+='<tr><td>'+obj[i]['pid']+'</td><td>'+obj[i]['0']+'</td><td>'+obj[i]['1']+'</td><td>'+obj[i]['2']+'</td></tr>';
                }
                $('#proDisplayTable').html(str);
            });
          }

          $.fn.table_refresher();
      //});
          $("#formPostProDis").validate({
            submitHandler:function(){
              var post_data = $("#formPostProDis").serialize()+"&action=loyalty-discount-lib_product&param=post_product_form_data";
              $.post(ajax_url,post_data,function(response){
                  //console.log(response);
                  if(response == 'N'){
                    alert("Product already exists!😵");
                  }
                  else{
                    $.fn.table_refresher();
                    alert("Product Successfully Added ✌");
                  }
              });
            }
          });

          $(document).on("keyup","#Upid",function(){
            var post_data ="&action=loyalty-discount-lib_product&param=get_product_form_data_of&Upid="+$('#Upid').val();
            $.post(ajax_url,post_data,function(response){
                var obj = JSON.parse(response);
                if(obj.length>0){
                  $('#UdisL').val(obj[0]['0']);
                  $('#UdisM').val(obj[0]['1']);
                  $('#UdisH').val(obj[0]['2']);
                }
            });
          });

          $("#formPostProDisUpdate").validate({
            submitHandler:function(){
              var post_data = $("#formPostProDisUpdate").serialize()+"&action=loyalty-discount-lib_product&param=update_product_form_data";
              $.post(ajax_url,post_data,function(response){
                  //console.log(response);
                  if(response == 'N'){
                    alert("Update Opretion failed!😵");
                  }
                  else{
                    $.fn.table_refresher();
                    alert("Product Successfully Updated ✌");
                  }
              });
            }
          });

          $("#formPostProDisDelete").validate({
            submitHandler:function(){
              var post_data = $("#formPostProDisDelete").serialize()+"&action=loyalty-discount-lib_product&param=delete_product_form_data";
              $.post(ajax_url,post_data,function(response){
                  //console.log(response);
                  if(response == 'N'){
                    alert("Delete Opretion failed!😵");
                  }
                  else{
                    $.fn.table_refresher();
                    alert("Product Successfully Deleted ✌");
                  }
              });
            }
          });

          //ON CLICK ADD NEW
          $(document).on("click",".addProductDis",function(){
            $("#formPostProDis").css("display","block");
            $("#btnAddProduct").css("display","block");
            $("#formPostProDisUpdate").css("display","none");
            $("#btnUpdateProduct").css("display","none");
            $('#formPostProDisDelete').css("display","none");
            $('#btnDeleteProduct').css("display","none");
          });

          //ON CLICK UPDATE
          $(document).on("click",".addProductDisUpdate",function(){
            $("#formPostProDis").css("display","none");
            $("#btnAddProduct").css("display","none");
            $("#formPostProDisUpdate").css("display","block");
            $("#btnUpdateProduct").css("display","block");
            $('#formPostProDisDelete').css("display","none");
            $('#btnDeleteProduct').css("display","none");
          });

          $(document).on("click",".addProductDisDelete",function(){
            $("#formPostProDis").css("display","none");
            $("#btnAddProduct").css("display","none");
            $("#formPostProDisUpdate").css("display","none");
            $("#btnUpdateProduct").css("display","none");
            $('#formPostProDisDelete').css("display","block");
            $('#btnDeleteProduct').css("display","block");
          });

        });

    </script>
  </head>
  <body>
    <h3><b>Product</b></h3>
    <div class="container">
      <h4><b>Product Discounts Management</b></h4>
      <button type="button" name="button" class="addProductDis btn btn-default">Add New</button>
      <button type="button" name="button" class="addProductDisUpdate btn btn-default">Update</button>
      <button type="button" name="button" class="addProductDisDelete btn btn-default">Delete</button>
        <div class="row">
          <form id="formPostProDis" style="display:none">
            <div class="col-xs-6">
              <label>Product ID</label>
              <input class="form-control" id="pid" required placeholder="Enter Product ID" name="pid">
              <br>
              <label>Product Discount</label><br>
              <div class="row">
                <div class="col-xs-4">
                  <label>Low Discount</label>
                  <input class="form-control" id="disL" required placeholder="Enter Discount" name="disL">
                </div>
                <div class="col-xs-4">
                  <label>Medium Discount</label>
                  <input class="form-control" id="disM" required placeholder="Enter Discount" name="disM">
                </div>
                <div class="col-xs-4">
                  <label>High Discount</label>
                  <input class="form-control" id="disH" required placeholder="Enter Discount" name="disH">
                  <br>
                </div>
                <div align="right">
                  <button type="submit" class="btn btn-default" id="btnAddProduct">Add Product</button>
                </div>
              </div>
            </div>
          </form>


          <form id="formPostProDisUpdate" style="display:none">
            <div class="col-xs-6">
              <label>Product ID</label>
              <input class="form-control" id="Upid" required placeholder="Enter Product ID" name="Upid">
              <br>
              <label>Product Discount</label><br>
              <div class="row">
                <div class="col-xs-4">
                  <label>Low Discount</label>
                  <input class="form-control" id="UdisL"  placeholder="Enter Discount" name="UdisL">
                </div>
                <div class="col-xs-4">
                  <label>Medium Discount</label>
                  <input class="form-control" id="UdisM"  placeholder="Enter Discount" name="UdisM">
                </div>
                <div class="col-xs-4">
                  <label>High Discount</label>
                  <input class="form-control" id="UdisH"  placeholder="Enter Discount" name="UdisH">
                  <br>
                </div>
                <div align="right">
                  <button type="submit" class="btn btn-default" id="btnUpdateProduct">Update Product</button>
                </div>
              </div>
            </div>
          </form>

          <form id="formPostProDisDelete" style="display:none">
            <div class="col-xs-6">
              <label>Product ID</label>
              <input class="form-control" id="Dpid" required placeholder="Enter Product ID" name="Dpid">
              <br>
                <div align="right">
                  <button type="submit" class="btn btn-default" id="btnDeleteProduct">Delete Product</button>
                </div>
            </div>
          </form>

          <div class="col-xs-6">
            <div id="ld_pro_table_size" class="">
              <table id="ProDisTable" class="table table-striped table-bordered">
                <thead>
                  <tr>
                    <tr>
                      <th>Product ID</th>
                      <th>Low</th>
                      <th>Medium</th>
                      <th>High</th>
                    </tr>
                  </tr>
                </thead>
                <tbody id="proDisplayTable">
                </tbody>
              </table>
            </div>
          </div>

        </div>

    </div>

  </body>
</html>
