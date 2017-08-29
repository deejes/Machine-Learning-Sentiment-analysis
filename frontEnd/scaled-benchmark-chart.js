var nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


var cloud_plot = [-0.10615000000000001, -0.07175000000000002, -0.09534999999999996, -0.10594999999999999, -0.08375000000000002, -0.11500000000000002, -0.11879999999999999, -0.06914999999999999, -0.10829999999999997, -0.12455000000000004,-1,1]

var custom_ml_plot = [-0.4360000000000005, -0.2360000000000003, -0.4240000000000003, -0.5320000000000003, -0.3840000000000005, -0.4720000000000003, -0.49200000000000044, -0.44000000000000034, -0.3920000000000003, -0.4120000000000003]

var happy_cloud = [0.8747999999999999, 0.6066, 0.6963999999999997, 0.5994999999999999, 0.6169999999999999, 0.66435, 0.4857500000000002, 0.69595, 0.6136999999999998, 0.70355]


var happy_custom = [0.40399999999999986, 0.6079999999999999, 0.572, 0.49599999999999994, 0.6919999999999998, 0.4959999999999999, 0.4799999999999999, 0.5839999999999997, 0.4439999999999999, 0.5159999999999999]


// For drawing the lines

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: nums,
    datasets: [
      {
        data: cloud_plot, label: "Cloud Analysis - #wtf", borderColor: "green", fill: false
      },
      {
        data: custom_ml_plot, label: "ML Analysis - #wtf", borderColor: "blue", fill: false
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
