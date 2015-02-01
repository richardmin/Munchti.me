$(document).ready(function() {
    loadOrders();
})

function loadOrders(){
    var ordersPromise = getPosts();

    ordersPromise = ordersPromise.then(function(orders, textStatus, jqXHR) {
        return $
    })
}
$('#orderForm').submit(function(event) {
    event.preventDefault();  

    function userFormError() {
        $('#orderError').html('<center>You have form errors. Please go back and ensure mandatory forms are filled.</center>');
        return;
    }


	function userOrderError() {
		$('#orderError').html(error('<center>We couldn\'t save your order. Please refresh and try again.</center><br />'));
		return;
	}
    function userOrderSuccess() {
        $('#orderError').html('<div data-alert class="alert-box success radius"><strong>We have recieved your order! Please refresh to submit a new one.</strong></div>');
        return;
    }
    var data = $('#orderForm').serializeObject();
<<<<<<< HEAD
    console.log(JSON.stringify(data));
    $.ajax({
        type: 'POST',
        url: '/api/post',
        data: JSON.stringify(data),
        contentType: 'application/json',
    }).done(function(order, textStatus, jqXHR) {
        window.location.replace("/");
        $("#submit").hide();
        userOrderSuccess();
    }).fail(function(error, textStatus, jqXHR) {
        userOrderError();
    });
});


=======
    if(data.name=="" || data.food=="" || data.destination==""|| data.time=="" || data.payment=="" || data.contact=="" )
    {
        userFormError();
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: '/api/post',
            data: JSON.stringify(data),
            contentType: 'application/json',
        }).done(function(order, textStatus, jqXHR) {
            $("#submit").hide();
            userOrderSuccess();
        }).fail(function(error, textStatus, jqXHR) {
            userOrderError();
        });
    }
});

$('')

// $(function() {
//     $('#orderForm').submit(function() {
//         $('#result').text(JSON.stringify($('#orderForm').serializeObject()));
//         return false;
//     });
// });
>>>>>>> b6b1396e55f93527bf6d63c654f743306c149fcb
