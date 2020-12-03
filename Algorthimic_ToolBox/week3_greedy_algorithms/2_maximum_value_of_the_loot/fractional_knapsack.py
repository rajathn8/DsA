# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    prop = []
    for i,j in zip(weights,values):
        prop.append(i/j)
    
    weight_capacity  = capacity
    total_revenue = 0
    sort_prop = sorted(prop,reverse=True) #nlogn

    for net in sort_prop: #n
        #print(net)
        if weight_capacity!=0:
            #supreme_index = prop.index(net) #n2
            available_weight_value = values[prop.index(net)]
            #print(weight_capacity,available_weight_value)
            weight_capacity = weight_capacity - available_weight_value
            if weight_capacity<0:
                #print(weight_capacity)
                partial_weight = (available_weight_value + weight_capacity)
                total_revenue = total_revenue  + net * (available_weight_value + weight_capacity)
                weight_capacity = 0
                #return total_revenue
            else:
                total_revenue = total_revenue  + net * available_weight_value



    return total_revenue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    #print(values)
    weights = data[3:(2 * n + 2):2]
    #print(weights)
    opt_value = get_optimal_value(capacity, weights =values , values = weights)
    print("{:.10f}".format(opt_value))
