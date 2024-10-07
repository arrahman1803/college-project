$(document).ready(function() {
    let product_color = $('.product-color').val();
    let product_size = $('.product-size').val();

    $(".add-to-cart-btn").on("click", function(){

    let this_val = $(this)
    let index = this_val.attr("data-index")
        let quantity = $('.product-quantity-' + index).val();
        let product_title = $('.product-title-' + index).val();
        let product_id = $('.product-id-' + index).val();
        let product_price = $('.product-price-' + index).text();
        let product_pid = $('.product-pid-' + index).val();
        let product_image = $('.product-image-' + index).val()
        console.log("qty", quantity);
        console.log("title", product_title);
        console.log("id", product_id);
        console.log("size", product_size);
        console.log("color", product_color);
        console.log("price", product_price);
        console.log("image", product_image);
        console.log("product pid", product_pid);

$.ajax({
    url : '/add-to-cart',
    data : {
    'id': product_id,
    'pid':product_pid,
    'image':product_image,
    'qty' : quantity,
    'title' : product_title,
    'size' : product_size,
    'color' : product_color,
    'price' : product_price,
    },
    dataType : 'json',
    beforeSend : function(){
    console.log("Adding Product.....");
    },
    success : function(response){
    this_val.html("Added To Cart")
    console.log("Added Product to Cart!");
    $(".cart-items-count").text(response.totalcartitems)
    }
    })

    });

    $('.product-color').on('change', function() {
        product_color = $(this).val(); // Update the variable
        console.log('Selected color:', product_color);
    });

    $('.product-size').on('change', function() {
        console.log('Change event fired');
        product_size = $(this).val(); // Update the variable
        console.log('Selected size:', product_size);
    });
 $(".delete-product").on("click", function(){
    let product_id = $(this).attr("data-product")
    let this_val = $(this)

    $.ajax({
    url : "/delete-from-cart",
    data : {
    "id" : product_id
    },
    dataType : "json",
    beforeSend : function(){
    this_val.hide()
    },
     success : function(response){
    this_val.show()
    $(".cart-items-count").text(response.totalcartitems)
    $('#cart-list').html(response.data)
    },
    })
    })
});

