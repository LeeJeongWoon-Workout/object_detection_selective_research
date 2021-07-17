bbox_list=[]
for gt_box in gt_list:
  bbox_list.append(extract_best_bbox(img_copy,gt_box))

cv_rectangle(img,gt_list,bbox_list)
visualization(img)
