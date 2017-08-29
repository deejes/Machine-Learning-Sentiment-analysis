import json
scores = [-0.6000000000000001, -0.6000000000000001, -1.0, 1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.19999999999999996, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.19999999999999996, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, 0.19999999999999996, 0.6000000000000001, -0.6000000000000001, 1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, 1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.19999999999999996, -0.19999999999999996, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.19999999999999996, 1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, 1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, 0.19999999999999996, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, 1.0, 0.19999999999999996, -1.0, -1.0, -0.6000000000000001, 1.0, 1.0, 1.0, 1.0, 1.0, 0.6000000000000001, 1.0, 1.0, -0.6000000000000001, -0.6000000000000001, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.6000000000000001, -1.0, 0.19999999999999996, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -0.6000000000000001, -0.19999999999999996, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, -1.0, 1.0, -0.19999999999999996, -0.19999999999999996, -0.6000000000000001, 1.0, 1.0, 1.0, 1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, 1.0, -1.0, -0.6000000000000001, -1.0, 0.19999999999999996, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, 0.19999999999999996, -0.6000000000000001, 0.19999999999999996, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.19999999999999996, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, 1.0, 1.0, 1.0, -0.6000000000000001, 1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, 0.19999999999999996, -1.0, -0.6000000000000001, 0.19999999999999996, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, 1.0, -1.0, 1.0, -0.19999999999999996, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.19999999999999996, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.19999999999999996, -1.0, 1.0, 1.0, -0.6000000000000001, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.19999999999999996, -0.6000000000000001, 0.19999999999999996, 1.0, 1.0, -1.0, 1.0, -0.6000000000000001, 1.0, 1.0, 1.0, 1.0, -0.6000000000000001, 1.0, 1.0, -0.6000000000000001, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 0.6000000000000001, 0.19999999999999996, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, 1.0, -1.0, 1.0, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.19999999999999996, -0.6000000000000001, 1.0, 1.0, 1.0, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, 0.19999999999999996, -0.6000000000000001, -0.6000000000000001, 0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.19999999999999996, 1.0, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, 1.0, -1.0, -0.6000000000000001, 1.0, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, 0.19999999999999996, 1.0, 1.0, -0.6000000000000001, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.19999999999999996, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, 0.19999999999999996, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.19999999999999996, -1.0, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.19999999999999996, -1.0, 1.0, -1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -0.6000000000000001, -1.0, 1.0, -1.0, -0.6000000000000001, 1.0, 1.0, -1.0, 1.0, -0.19999999999999996, -1.0, -0.6000000000000001, 0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, 0.19999999999999996, -1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -1.0, 1.0, -1.0, -0.6000000000000001, -0.19999999999999996, -1.0, -1.0, 1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, 1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.19999999999999996, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, -1.0, -1.0, 0.19999999999999996, 1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, 1.0, -1.0, -1.0, -1.0, 0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, 0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.19999999999999996, 1.0, -1.0, -0.6000000000000001, -0.19999999999999996, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, 0.19999999999999996, 1.0, -0.6000000000000001, 1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 0.19999999999999996, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.19999999999999996, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, 1.0, -0.19999999999999996, 1.0, -1.0, 1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.19999999999999996, 0.19999999999999996, -1.0, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -1.0, 0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, 1.0, -1.0, -0.6000000000000001, 1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.6000000000000001, -1.0, -0.6000000000000001, -1.0, -1.0, -0.6000000000000001, -0.19999999999999996, -1.0, -1.0, -1.0, 1.0, -0.19999999999999996, -1.0, -0.6000000000000001, -1.0, -1.0]




plot_points = []
start = 0
end = 100

while True:
    # print
    total = 0
    try:
        for x in range(start,end):
            total += scores[x]
        plot_points.append(total/100)
        start +=100
        end += 100
    except:
        break

print (plot_points)
# print (len(mags))
#
# with open("wtf_cloud_plotpoints.txt","w") as f:
#     json.dump(plot_points,f)
#
# print ([x for x in range(1,len(mags))])
