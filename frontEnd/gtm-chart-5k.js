var years = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

// For drawing the lines

var monsantoSentiment = [-0.29561752988047574, -0.3816733067729062, -0.42868525896414106, -0.5306772908366515, -0.564940239043824, -0.50836653386454, -0.48844621513943953, -0.10278884462151318, -0.33705179282868286, -0.3370517928286829]

var googleSentiment = [-0.36573705179282684, -0.42151394422310556, -0.38804780876493794, -0.4047808764940222, -0.45976095617529594, -0.4685258964143401, -0.45657370517928014, -0.4828685258964117, -0.5075697211155348, -0.5035856573705147,1,-1]

var teslaSentiment = [-0.39005964214711514, -0.44333996023856675, -0.4282306163021848, -0.7009940357852931, -0.34473161033797056, -0.2159045725646112, -0.36063618290258276, -0.2954274353876726, -0.464811133200793, -0.34950298210735364]



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
