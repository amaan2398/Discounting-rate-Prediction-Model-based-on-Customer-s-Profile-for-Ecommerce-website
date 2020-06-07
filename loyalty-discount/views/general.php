<?php
 ?>

 <!DOCTYPE html>
 <html lang="en" dir="ltr">
   <head>
     <meta charset="utf-8">
     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.16.0/jquery.validate.min.js"></script>
     <script>
       $(function(){
         $("#formPostTaxStatus").validate({
           submitHandler:function(){
           var post_data = $("#formPostTaxStatus").serialize()+"&action=loyalty-discount-lib_general&param=post_general_form_data";
           $.post(ajax_url,post_data,function(response){
               //console.log(response);
               if(response == 'N'){
                 alert("Product already exists!😵");
               }
               else{
                 alert("Product Successfully Added ✌");
               }
           });
           //$('#tax_toggle').prop( "checked", false );
          }
         });
       });
     </script>
     <style>
        .center{
          position: absolute;
          transform: scale(1.8);
        }
        label#note{
          font-size: 12px;
        }
     </style>
   </head>
   <body>
     <h3><b>Settings</b></h3>
     <div class="container">
       <h4><b>General Settings</b></h4>
       <div class="row">
         <div class="col-xs-6">
           <h5><b>TAX</b></h5>
           <form id="formPostTaxStatus">
             <div class="row">
               <div class="col-xs-6">
                 <input type="checkbox" class="center" id="tax_toggle" name="tax_toggle">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                 <label id="note">Check If TAX Apply to Discount</label><br><br>
                 <button type="submit" class="btn btn-default" id="btnSave">Save</button>
               </div>
             </div>
           </form>
         </div>
       </div>
     </div>
   </body>
 </html>
