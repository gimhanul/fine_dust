var state = 0;
// ['0':'none', '1':'good','2':'normal','3':'bad','4':'sobad']

$(document).ready(function () {
    setTimeout(function(){
        location.reload();
    },120000); // 2분
    
    //마우스를 올려놓았을때 이벤트
    mouseListener();

    // 서버 단 연결 
    // data 를 받아서 state에 저장
    let element = document.getElementById('dust');
    // alert(element.innerText);

    data = parseInt(element.innerText);
    data = data.toFixed(2);

    if (data < 16) {
        state = 1;
    }
    else if (data >= 16 && state < 36) {
        state = 2;
    }
    else if (state >= 36 && state < 76) {
        state = 3;
    }
    else if (state >= 76) {
        state = 4;
    }

    // $.ajax({
    //     url: '/rankdata',
    //     type: 'GET',
    //     dataType: 'json',
    //     // data로 농도를 받음
    //     success: function (data) {
    //         alert(data);
    //         state = data.parseFloat();
    //         if (state < 16) {
    //             state = 1;
    //         }
    //         else if (state >= 16 && state < 36) {
    //             state = 2;
    //         }
    //         else if (state >= 36 && state < 76) {
    //             state = 3;
    //         }
    //         else if (state >= 76) {
    //             state = 4;
    //         }
    //     },
    //     error: function (request, status, error) {
    //         alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);

    //     },
    // })

    changeURL(state, data);
})

const changeURL = (state, data) => {
    //good
    if (state == 1) {
        $("title").html("good")
        $("#dust").html(data)
    }
    //normal
    else if (state == 2) {
        $("title").html("normal")
        $("body").css("background-color", "rgba(108,184,107, 0.3)")
        $("#dust").html(data)
        $(".good").css("background-image", "src({{url_for('static', filename='image/normal.png')}})")
        $(".good").attr({ "src": "{{url_for('static', filename='image/normal.png')}}", "class": "good" })
        $("p").css({ "color": "#6CB86B" })
        $("p#dust").css({ "background-color": "rgba(255,255,255,0.4)" })
        $(".last").html("애매하네....")
    }
    //bad
    else if (state == 3) {
        $("title").html("bad")
        $("body").css("background-color", "rgba(234,215,46,0.3)")
        $("#dust").html(data)
        $(".good").attr({ "src": "{{url_for('static', filename='image/bad.png')}}", "class": "good" })
        $("p").css({ "color": "#D0BC0A" })
        $("p#dust").css({ "background-color": "rgba(255,255,255,0.4)" })
        $(".last").html("마스크 여매고 댕겨라,,,끌끌,,,")
    }
    //sobad
    else if (state == 4) {
        $("title").html("sobad")
        $("body").css("background-color", "rgba(184,107,107,0.5)")
        $("#dust").html(data)
        $(".good").attr({ "src": "{{url_for('static', filename='image/sobad.png')}}", "class": "good" })
        $("p").css({ "color": "#B86B6B" })
        $("p#dust").css({ "background-color": "rgba(255,255,255,0.4)" })
        $(".last").html("당장 공기청정기 켜!!...")
    }
    //ajax 값이 들어오지 않고 0일때 
    else {
        $("title").html("error")
        $(".first").html("ERROR")
        $("body").css({
            "background-color": "rgba(255,0, 0, 0.5)",
            "margin-left": "300px"
        })
        for (var i = 1; i < 3; i++) {
            $("p").eq(i).remove()
        }
        $("p").remove("#dust")
        $("img").remove()
        $(".first").css({
            "font-size": "5.5em",
            "color": "white",
            "margin-left": "330px",
            "margin-top": "280px"
        })
    }
}

const mouseListener = () => {
    // class dust에 마우스가 올라갔을 때
    $("p#dust").on("mouseenter", function (event) {
        $(this).css("transform", "scale(1.1)");
    })
    $("p#dust").on("mouseleave", function (event) {
        $(this).css("transform", "scale(1)")
        $(this).css({
            "-webkit-transform": "rotate(-10deg)",
            "transform": "rotate(-10deg)",
            "font-size": "50px",
            "margin-left": "10em",
            "display": "inline-block",
            "margin-left": "5.5em",
            "font-size": "100px",
            "margin-bottom": "0px",
            "margin-top": "0px",
        })
    })
}
