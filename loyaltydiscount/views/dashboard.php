<?php  ?>
 <!DOCTYPE html>
 <html lang="en">
 <head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
   <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.16.0/jquery.validate.min.js"></script>

   <script>
       $(function() {
         var chartPL;

             var post_data = "action=loyalty-discount-lib_dashboard&param=get_dashboad_data";
             $.post(ajax_url,post_data,function(response){
                 var obj = JSON.parse(response);
                 var dis = parseInt(obj[0]['dis']);
                 var price = parseInt(obj[0]['price']);
                 var tsales= dis + price;
                 $("#tsales").html('₹'+tsales.toString(10));
                 $("#nsales").html('₹'+price.toString(10));
                 $("#tdis").html('₹'+dis.toString(10));
                 $("#cord").html(obj[0]['cord']);
             });


         });
   </script>

   <script>
   $(function(){
     var colour_chart_line = '#186dd6';
     const getDaysInMonth = date => new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
     var post_data = "action=loyalty-discount-lib_dashboard&param=get_dashboad_chart_data";
     $.post(ajax_url,post_data,function(response){
         var obj = JSON.parse(response);
         var i;
         var tsales_lable=[];
         var tsales_datat=[];
         var tsales_datan=[];
         var tsales_datad=[];
         var tsales_datao=[];
         var todayDate=new Date().getDate();
         for(i=1;i<=obj.length;i++){
           tsales_datat.push(0);
           tsales_datan.push(0);
           tsales_datad.push(0);
           tsales_datao.push(0);
           tsales_lable.push(obj[i-1]['date']+"-"+obj[i-1]['month']+"-"+obj[i-1]['year']);
         }
         var temp;
         var km=0;
         for(i=0;i<obj.length;i++){
           temp=(parseInt(obj[i]['price'])+parseInt(obj[i]['discount']));
           if(parseInt(obj[i]['date']) == 1 && i>0){
             km+=i-km;
           }
           tsales_datat[parseInt(obj[i]['date'])-1+km]=temp;
         }

         var ctx = document.getElementById('ld-tsales_chart').getContext('2d');
         var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: tsales_lable,
                datasets: [{
                    label: 'TOTAL SALES',
                    borderColor: colour_chart_line,
                    data: tsales_datat
                }]
            },

            // Configuration options go here
            options: {
              title: {
                   display: true,
                   text: 'TOTAL SALES',
                   fontSize: 15
               },
               legend:{
                 display:false
               },
               layout: {
                   padding: 0
               },
               scales: {
                    yAxes: [{
                        ticks: {
                            // Include a dollar sign in the ticks
                            callback: function(value, index, values) {
                                return '₹' + value;
                            }
                        }
                    }]
                }
            }
         });



         var ctx = document.getElementById('ld-nsales_chart').getContext('2d');
         km=0;
         for(i=0;i<obj.length;i++){
           if(parseInt(obj[i]['date']) == 1 && i>0){
             km+=i-km;
           }
           tsales_datan[parseInt(obj[i]['date'])-1+km]=parseInt(obj[i]['price']);
         }
         var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: tsales_lable,
                datasets: [{
                    label: 'NET SALES',
                    borderColor: colour_chart_line,
                    data: tsales_datan
                }]
            },

            // Configuration options go here
            options: {
              title: {
                   display: true,
                   text: 'NET SALES',
                   fontSize: 15
               },
               legend:{
                 display:false
               },
               layout: {
                   padding: 0
               },
               scales: {
                    yAxes: [{
                        ticks: {
                            // Include a dollar sign in the ticks
                            callback: function(value, index, values) {
                                return '₹' + value;
                            }
                        }
                    }]
                }
            }
         });



         var ctx = document.getElementById('ld-discount_chart').getContext('2d');
         km=0;
         for(i=0;i<obj.length;i++){
           if(parseInt(obj[i]['date']) == 1 && i>0){
             km+=i-km;
           }
           tsales_datad[parseInt(obj[i]['date'])-1+km]=parseInt(obj[i]['discount']);
         }
         var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: tsales_lable,
                datasets: [{
                    label: 'TOTAL DISCOUNT',
                    borderColor: colour_chart_line,
                    data: tsales_datad
                }]
            },

            // Configuration options go here
            options: {
              title: {
                   display: true,
                   text: 'TOTAL DISCOUNT',
                   fontSize: 15
               },
               legend:{
                 display:false
               },
               layout: {
                   padding: 0
               },
               scales: {
                    yAxes: [{
                        ticks: {
                            // Include a dollar sign in the ticks
                            callback: function(value, index, values) {
                                return '₹' + value;
                            }
                        }
                    }]
                }
            }
         });


         var ctx = document.getElementById('ld-order_chart').getContext('2d');
         km=0;
         for(i=0;i<obj.length;i++){
           if(parseInt(obj[i]['date']) == 1 && i>0){
             km+=i-km;
           }
           tsales_datao[parseInt(obj[i]['date'])-1+km]=parseInt(obj[i]['ord']);
         }
         var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'line',

            // The data for our dataset
            data: {
                labels: tsales_lable,
                datasets: [{
                    label: 'ORDERS',
                    borderColor: colour_chart_line,
                    data: tsales_datao
                }]
            },

            // Configuration options go here
            options: {
              title: {
                   display: true,
                   text: 'ORDERS',
                   fontSize: 15
               },
               legend:{
                 display:false
               },
               layout: {
                   padding: 0
               }
            }
         });




     });
   });
   </script>

 </head>
 <body>
   <h2><b>Dashboard</b></h2>
   <div class="container">
      <h2>Performance</h2>
      <div class="list-group">
        <a class="list-group-item col-sm-4">
          <p class="list-group-item-text">TOTAL SALES</p><br>
          <h4 class="list-group-item-heading" id="tsales"> </h4>
        </a>
        <a class="list-group-item col-sm-4">
          <p class="list-group-item-text">NET SALES</p><br>
          <h4 class="list-group-item-heading" id="nsales"></h4>
        </a>
        <a class="list-group-item col-sm-4">
          <p class="list-group-item-text">TOTAL DISCOUNT</p><br>
          <h4 class="list-group-item-heading" id="tdis"></h4>
        </a>
        <a class="list-group-item col-sm-4">
          <p class="list-group-item-text">ORDERS</p><br>
          <h4 class="list-group-item-heading" id="cord"></h4>
        </a>
    </div>
  </div>
  <div class="container">
    <h2>Charts</h2>
    <div class="list-group ">
      <div class="list-group-item col-lg-6">
        <canvas id="ld-tsales_chart"></canvas>
      </div>
      <div class="list-group-item col-lg-6">
        <canvas id="ld-nsales_chart"></canvas>
      </div>
      <div class="list-group-item col-lg-6">
        <canvas id="ld-discount_chart"></canvas>
      </div>
      <div class="list-group-item col-lg-6">
        <canvas id="ld-order_chart"></canvas>
      </div>
    </div>
  </div>
 </body>
 </html>
