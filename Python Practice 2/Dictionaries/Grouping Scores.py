def grouping_scores(ball_score_list):
    dictionary_a={}
    for item in ball_score_list:
        pair=item.split(":")
      
        color, score =pair[0], int(pair[1])
       

        if color in dictionary_a:
            dictionary_a[color]=dictionary_a[color]+score
        else:
            dictionary_a[color]=score
    return dictionary_a
 
ball_score_list=input().split(",")
dictionary_a=grouping_scores(ball_score_list)
print(dictionary_a)