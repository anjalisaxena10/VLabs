utils = {
    getQuizzes: function() {
	    var xhr = new XMLHttpRequest()
	    console.log("utils::getQuizzes")
	    
        xhr.onload = function() {
	        console.log("xhr::onload: ", this.responseText);
	    }

	    xhr.open("GET", "http://127.0.0.1:54321/quizzes", true)
	    
	    xhr.onerror = (function(e) {
	    	console.log("xhr::send error: " +  e)
            this.reportError(e)
        }).bind()

        xhr.send()
    },

    reportError: function(e) {
    	for (var property in e) {
            if (e.hasOwnProperty(property)) {
                console.log(property + ": " + e[property])
            }
        }
    }
}


