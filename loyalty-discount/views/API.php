
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <style>
    .btn{
      margin-bottom: 10px;
    }
    .scrollable{
      width: 100%;
      height: 200px;
      overflow-y: scroll;
    }
  </style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.16.0/jquery.validate.min.js"></script>
  <script>
  $(function(){
    $.fn.key_table_refresher=function(){
      var post_data = "&action=loyalty-discount-lib_api&param=get_api_key_data";
      $.post(ajax_url,post_data,function(response){
          console.log(response);
          var obj = JSON.parse(response);
          var i =0;
          var str='';
          if(obj.length>8){
            $('#ld_key_table_size').addClass('scrollable');
          }
          else{
            $('#ld_key_table_size').removeClass('scrollable');
          }
          for(i=0;i<obj.length;i++){
            str+='<tr><td>'+obj[i]['key_id']+'</td><td>'+obj[i]['description']+'</td><td>...'+obj[i]['security_key'].slice(obj[i]['security_key'].length-4)+'</td></tr>';
          }
          $('#keyDisplayTable').html(str);
      });
    }

    $.fn.key_table_refresher();

    $("#formPost").validate({
      submitHandler:function(){
        var post_data = $("#formPost").serialize()+"&action=loyalty-discount-lib_api&param=post_api_form_data";
        $.post(ajax_url,post_data,function(response){
            $('#apiSKey').html(response);
            $('#securityKey').css("display","block");
            $('#btnGenerate').css("display","none");
            if(response == 'N'){
              alert("Product already exists!😵");
            }
            else{
              $.fn.key_table_refresher();
              alert("Product Successfully Added ✌");
            }
        });
      }
    });

    $("#formPostDelete").validate({
      submitHandler:function(){
        var post_data = $("#formPostDelete").serialize()+"&action=loyalty-discount-lib_api&param=post_api_delete_data";
        $.post(ajax_url,post_data,function(response){
            if(response == 'N'){
              alert("Product already exists!😵");
            }
            else{
              $.fn.key_table_refresher();
              alert("Product Successfully Added ✌");
            }
        });
      }
    });

    $(document).on("click",".createAPIKeyView",function(){
      $("#formPost").css("display","block");
      $("#btnGenerate").css("display","block");
      $("#securityKey").css("display","none");
      $("#formPostDelete").css("display","none");
      $("#btnDelete").css("display","none");
    });

    $(document).on("click",".createAPIKeyDelete",function(){
      $("#formPost").css("display","none");
      $("#btnGenerate").css("display","none");
      $("#securityKey").css("display","none");
      $("#formPostDelete").css("display","block");
      $("#btnDelete").css("display","block");
    });
  });

  </script>
</head>
<body>
<h3><b>API</b></h3>
<div class="container">
  <h4><b>Get Your API key</b></h4>
  <button type="button" name="button" class="createAPIKeyView btn btn-default">Create</button>
  <button type="button" name="button" class="createAPIKeyDelete btn btn-default">Discard/Remove Key</button>
  <br>
  <div class="row">
    <form id="formPost" style="display:none">
      <div class="col-xs-4">
        <label>Description:</label>
        <input class="form-control" id="description" placeholder="Enter description" name="description">
        <br>
        <div align="right">
          <button type="submit" class="btn btn-default" id="btnGenerate">Generate</button>
        </div>
      </div>
      <div class="col-xs-4" id='securityKey' style='display:none'>
        <label>Security Key:</label>
        <label class="form-control" id='apiSKey'></label>
      </div>
    </form>

    <form id="formPostDelete" style="display:none">
      <div class="col-xs-4">
        <label>ID:</label>
        <input class="form-control" id="api_id" placeholder="Enter ID" name="api_id">
        <br>
        <div align="right">
          <button type="submit" class="btn btn-default" id="btnDelete">Delete key</button>
        </div>
      </div>
    </form>

    <div class="col-xs-6">
      <div id="ld_key_table_size" class="">
        <table id="KeyDisTable" class="table table-striped table-bordered">
          <thead>
            <tr>
              <tr>
                <th>ID</th>
                <th>Description</th>
                <th>Key</th>
              </tr>
            </tr>
          </thead>
          <tbody id="keyDisplayTable">
          </tbody>
        </table>
      </div>
    </div>

  </div>
</div>

</body>
</html>
