$('#orderForm').submit(function(event) {
    event.preventDefault();  

	function userOrderError() {
		$('#orderError').html(error('<center>We couldn\'t save your order. Please refresh and try again.</center>'));
		return;
	}
    function userOrderSuccess() {
        $('#orderError').html('<center>We have recieved your order! Please refresh to submit a new one.</center>');
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
        userOrderSuccess();
    }).fail(function(error, textStatus, jqXHR) {
        userOrderError();
    });
});

// $(function() {
//     $('#orderForm').submit(function() {
//         $('#result').text(JSON.stringify($('#orderForm').serializeObject()));
//         return false;
//     });
// });
