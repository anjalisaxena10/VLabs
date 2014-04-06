view = {
    init: function() {
        var next = document.getElementById("nextQuiz")
        next.addEventListener("click", utils.getQuizzes)
        console.log("view::init()")
    }
}

function main() {
	view.init()
}

window.addEventListener("load", main)
