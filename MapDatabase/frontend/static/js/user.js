var token = $('input[name="csrfmiddlewaretoken"]').prop('value');

function updateSelect(time_from, time_to) {
      $.ajax({
	    url: '',
	    method: 'post',
	    data: {
	        "type": "select",
	        "time_from": time_from,
	        "time_to": time_to,
	        'csrfmiddlewaretoken': token
	    },
	    success: function(data){
	        console.log(data)
	        console.log("success");
	    },
	    error: function(){
		    console.log("error");
	    }
    });
}

function updateCurrent() {
      $.ajax({
	    url: '',
	    method: 'post',
	    data: {
	        "type": "current",
	        'csrfmiddlewaretoken': token
	    },
	    success: function(data){
	        console.log(data)
	        console.log("success");
	    },
	    error: function(){
		    console.log("error");
	    }
    });
}

$("#time_from").change(function(){
   updateSelect($("#time_from")[0].value, $("#time_to")[0].value)
});

$("#time_to").change(function(){
     updateSelect($("#time_from")[0].value, $("#time_to")[0].value)
});

//setInterval(updateCurrent, 10*60*1000)