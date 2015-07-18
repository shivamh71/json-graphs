	function sendtext(){
			console.log("hello");
			$.ajax({
				type : "POST",
				url: "http://localhost:5000/convert",
				data: $('#dataText').val(),
				success: function(data){
					console.log(data);
				},
				error: function(err){
					console.log(err);
				}
			})
		}
