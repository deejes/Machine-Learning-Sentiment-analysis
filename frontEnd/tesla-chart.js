var years =["Aug 12 01:57:-22:20", " Aug 11 22:20-19:14", " Aug 11 19:14-16:45", " Aug 11 16:45-15:34", " Aug 11 15:34-13:45", " Aug 11 13:45-11:26", " Aug 11 11:26-07:58", " Aug 11 07:58-04:30", " Aug 11 04:30-01:03", " Aug 11 01:02-21:29"]


var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: sentiment, fill: false
      // } ,
      // {
      //   data: latinAmerica, label: "SA", borderColor: "green", fill: false
      // } ,
      // {
      //   data: asia, label: "asia", borderColor: "red", fill: false
      // } ,
      // {
      //   data: europe, label: "EUR", borderColor: "blue", fill: false
    }
  ]

  },
  //  {
  //   responsive: true,
  //   maintainAspectRatio: false
  // },
options: {
    responsive: true,
    maintainAspectRatio: true,
    // scaleOverride: true,
    // scaleStartValue: 0,
    // legend: {
    //     position: 'bottom',
    // },
    // hover: {
    //     mode: 'label'
    // },
    // scales: {
    //     xAxes: [{
    //             display: true,
    //             scaleLabel: {
    //                 display: true,
    //                 labelString: 'Month'
    //             }
    //         }],
    yAxes: [{
      display: true,
      ticks: {
        beginAtZero: true,
        // steps: 10,
        // stepValue: 5,
        max: 1,
        min: -1
      }
    }]
    // },
    // title: {
    //     display: true,
    //     text: 'Chart.js Line Chart - Legend'
    // }
  }
});

//
// options: {
//        scales: {
//            yAxes: [{
//                ticks: {
//                    suggestedMin: 50
//                    suggestedMax: 100
//                }
//            }]
//        }
//    }
