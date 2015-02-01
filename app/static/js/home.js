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

	function userOrderError() {
		$('#orderError').html(error('<center>We couldn\'t save your order. Please refresh and try again.</center>'));
		return;
	}
    function userOrderSuccess() {
        $('#orderError').html('<div data-alert class="alert-box success radius"><strong>We have recieved your order! Please refresh to submit a new one.</strong></div>');
        return;
    }
    var data = $('#orderForm').serializeObject();
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


