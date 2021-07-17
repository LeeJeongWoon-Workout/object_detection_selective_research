def cv_rectangle(img,gt_list,bbox):
  for i in range(len(gt_list)):
    img=cv2.rectangle(img,(gt_list[i][0],gt_list[i][1]),(gt_list[i][2],gt_list[i][3]),color=(255,0,0),thickness=3)
    img=cv2.rectangle(img,(bbox_list[i][-1][0],bbox_list[i][-1][1]),(bbox_list[i][-1][2],bbox_list[i][-1][3]),color=(0,255,0),thickness=2)

def visualization(img):
  plt.figure(figsize=(8,8))
  plt.imshow(img)
  plt.show()

def compute_iou(c_box,g_box):
  x1=np.maximum(c_box[0],g_box[0])
  y1=np.maximum(c_box[1],g_box[1])
  x2=np.minimum(c_box[2],g_box[2])
  y2=np.minimum(c_box[3],g_box[3])

  intersection=np.maximum(x2-x1,0)*np.maximum(y2-y1,0)
  c_area=(c_box[2]-c_box[0])*(c_box[3]-c_box[1])
  g_area=(g_box[2]-g_box[0])*(g_box[3]-g_box[1])

  union=c_area+g_area-intersection

  return intersection/union


def extract_best_bbox(img,gt_box):
  _,regions=selectivesearch.selective_search(img,scale=200,min_size=1000)
  iou_list=[]
  cand_rect=[cand['rect'] for cand in regions]

  for cand_box in cand_rect:
    cand_box=list(cand_box)
    cand_box[2]+=cand_box[0]
    cand_box[3]+=cand_box[1]

    iou=compute_iou(cand_box,gt_box)
    iou_list.append([iou,cand_box])

  return max(iou_list)
