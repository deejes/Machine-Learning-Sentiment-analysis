var years =['8/10 21:28', '', '', ' ', ' ', '', '', ' ', ' ', ' 8/17 19:03']

// For drawing the lines
var africa = [86,114,106,106,107,111,133,221,783,2478];
var asia = [282,350,411,502,635,809,947,1402,3700,5267];
var europe = [168,170,178,190,203,276,408,547,675,734];
var latinAmerica = [40,20,10,16,24,38,74,167,508,784];
var northAmerica = [226,3,2,2,7,26,82,172,312,433];
var monsantoSentiment = [-0.7757338551859152, -0.6880626223092018, -0.6849315068493177, -0.8027397260273993, -0.588258317025444, -0.441878669275932, -0.4003913894324861, -0.3866927592955002, -0.79804305283758, -0.8000000000000071, 1, -1]

var googleSentiment = [-0.4936398467432934, -0.5629118773946314, -0.588965517241374, -0.6568582375478825, -0.5494252873563166, -0.4573180076628352, -0.5471264367816041, -0.5334865900383104, -0.5977011494252801, -0.47862068965516824,-1,1]

var teslaSentiment = [-0.42772925764192543, -0.38624454148471976, -0.41724890829694655, -0.5860262008733648, -0.4884279475982565, -0.4716157205240218, -0.5609170305676905, -0.20414847161572178, -0.20393013100436808, -0.20393013100436808,-1,1]

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: googleSentiment, label: "Google", borderColor: "green", fill: false
      } ,
      {
        data: teslaSentiment, label: "Tesla", borderColor: "red", fill: false
      } ,
      {
        data: monsantoSentiment, label: "Monsanto", borderColor: "blue", fill: false
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
