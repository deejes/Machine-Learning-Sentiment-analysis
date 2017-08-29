var nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


var cloud_plot = [-0.21230000000000002, -0.14350000000000004, -0.19069999999999993, -0.21189999999999998, -0.16750000000000004, -0.23000000000000004, -0.23759999999999998, -0.13829999999999998, -0.21659999999999993, -0.24910000000000007,1,-1]

var custom_ml_plot = [-0.4360000000000005, -0.2360000000000003, -0.4240000000000003, -0.5320000000000003, -0.3840000000000005, -0.4720000000000003, -0.49200000000000044, -0.44000000000000034, -0.3920000000000003, -0.4120000000000003]

var happy_cloud = [1.7495999999999998, 1.2132, 1.3927999999999994, 1.1989999999999998, 1.2339999999999998, 1.3287, 0.9715000000000004, 1.3919, 1.2273999999999996, 1.4071]

var happy_custom = [0.40399999999999986, 0.6079999999999999, 0.572, 0.49599999999999994, 0.6919999999999998, 0.4959999999999999, 0.4799999999999999, 0.5839999999999997, 0.4439999999999999, 0.5159999999999999]


// For drawing the lines

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: nums,
    datasets: [
      {
        data: cloud_plot, label: "Cloud Analysis - #WTF", borderColor: "green", fill: false
      },
      {
        data: custom_ml_plot, label: "ML Analysis - #WTF", borderColor: "blue", fill: false
      },
      {
        data: happy_cloud, label: "Cloud Analysis - #happy", borderColor: "red", fill: false
      },
      {
        data: happy_custom, label: "ML Analysis - #happy", borderColor: "pink", fill: false
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
