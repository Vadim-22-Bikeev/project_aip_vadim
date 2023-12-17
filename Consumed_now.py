def consumed_now(pr_wight,pr_cal,pr_prot,pr_fat,pr_carb):#Калорийность вводится на 100 грамм продукта 
    sum_cal = (pr_cal * pr_wight) / 100                  
    sum_prot = (pr_prot * pr_wight) / 100
    sum_fat = (pr_fat * pr_wight) / 100
    sum_carb = (pr_carb * pr_wight) / 100
    return round(sum_cal), round(sum_prot), round(sum_fat), round(sum_carb)