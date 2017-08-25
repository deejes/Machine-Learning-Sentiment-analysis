var years =['00:45:-00:02', ' 00:01-22:50', ' 22:50-22:02', ' 22:00-21:19', ' 21:13-20:01', ' 20:00-19:21', ' 19:20-18:23', ' 18:21-17:53', ' 17:52-17:22', ' 17:22-16:46']

// For drawing the lines
var africa = [86,114,106,106,107,111,133,221,783,2478];
var asia = [282,350,411,502,635,809,947,1402,3700,5267];
var europe = [168,170,178,190,203,276,408,547,675,734];
var latinAmerica = [40,20,10,16,24,38,74,167,508,784];
var northAmerica = [226,3,2,2,7,26,82,172,312,433];



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
