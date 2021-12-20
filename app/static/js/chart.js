// 들어오는 값
var valuelist = [];

var currentdate = new Date();
console.log(currentdate);
var mm = String(currentdate.getMonth() + 1).padStart(2, '0'); //January is 0!
var dd = String(currentdate.getDate()).padStart(2, '0');
dd = Number(dd);
console.log(`${mm}/${dd}`)
// 우선 컨텍스트를 가져옵니다. 
var ctx = document.getElementById("myChart").getContext('2d');
/*
- Chart를 생성하면서, 
- ctx를 첫번째 argument로 넘겨주고, 
- 두번째 argument로 그림을 그릴때 필요한 요소들을 모두 넘겨줍니다. 
*/
datelist = [];
for (var i = 0; i < 6; i++) {
    if (dd - i < 1) {
        if (mm < 8 && mm%2==1 || mm>=8 && mm%2==0){ // mm 이 1, 3, 5, 7, 8, 10, 12
            dd = (dd-i)+31
        }
        else{
            dd = (dd-i)+30
        }
        if(mm == 1){ // 1월일때 12월로 변환
            mm = 12
        }
    }
    datelist.push(`${mm}/${dd - i}`)
}

var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [datelist[5], datelist[4], datelist[3], datelist[2], datelist[1], datelist[0]],
        datasets: [{
            label: '# 미세먼지 그래프',
            data: valuelist,
            backgroundColor: [
                // 'rgba(255, 99, 132, 0.2)',
                // 'rgba(54, 162, 235, 0.2)', 
                // 'rgba(255, 206, 86, 0.2)',
                // 'rgba(75, 192, 192, 0.2)', 
                'rgba(153, 102, 255, 0.2)',
                // 'rgba(255, 159, 64, 0.2)' 
            ],
            borderColor: [
                // 'rgba(255,99,132,1)', // 빨간색
                // 'rgba(54, 162, 235, 1)', // 파란색
                // 'rgba(255, 206, 86, 1)', // 노랑
                // 'rgba(75, 192, 192, 1)', // 하늘
                'rgba(153, 102, 255, 1)', // 보라
                // 'rgba(255, 159, 64, 1)' //연주황
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: true, // default value. false일 경우 포함된 div의 크기에 맞춰서 그려짐.
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

$(document).ready(function(){
    $.ajax({
        url: '/chart',
        type: 'GET',
        dataType: 'json',
        // data로 농도를 받음
        success: function (data) {
            
            //code
        },
        error: function (request, status, error) {
            alert("code:" + request.status + "\n" + "message:" + request.responseText + "\n" + "error:" + error);
        },
    })
})