def difference(vals_r , vals_f):
    w = {'+': 'больше на', '-': 'ниже на', '0' : 'столько же,сколько ожидалось'}
    dif = list()
    for i in range(0,4):
      pred_res = vals_f[i]-vals_r[i]
      dop = list()
      if pred_res > 0:
        a = '+'
        dop.append(w[a]) 
        dop.append(pred_res)
      elif pred_res < 0:
        b = '-'
        dop.append(w[b])
        dop.append(pred_res)
      elif pred_res == 0:
        c ='0'
        dop.append(w[c])
        dop.append(pred_res)
      dif.append(dop)
    return dif