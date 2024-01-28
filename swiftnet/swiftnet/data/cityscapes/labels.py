from collections import namedtuple

#--------------------------------------------------------------------------------
# Definitions
#--------------------------------------------------------------------------------

# a label and all meta information
Label = namedtuple( 'Label' , [

    'name'        , # The identifier of this label, e.g. 'car', 'person', ... .
                    # We use them to uniquely name a class

    'id'          , # An integer ID that is associated with this label.
                    # The IDs are used to represent the label in ground truth images
                    # An ID of -1 means that this label does not have an ID and thus
                    # is ignored when creating ground truth images (e.g. license plate).
                    # Do not modify these IDs, since exactly these IDs are expected by the
                    # evaluation server.

    'trainId'     , # Feel free to modify these IDs as suitable for your method. Then create
                    # ground truth images with train IDs, using the tools provided in the
                    # 'preparation' folder. However, make sure to validate or submit results
                    # to our evaluation server using the regular IDs above!
                    # For trainIds, multiple labels might have the same ID. Then, these labels
                    # are mapped to the same class in the ground truth images. For the inverse
                    # mapping, we use the label that is defined first in the list below.
                    # For example, mapping all void-type classes to the same ID in training,
                    # might make sense for some approaches.
                    # Max value is 255!

    'category'    , # The name of the category that this label belongs to

    'categoryId'  , # The ID of this category. Used to create ground truth images
                    # on category level.

    'hasInstances', # Whether this label distinguishes between single instances or not

    'ignoreInEval', # Whether pixels having this class as ground truth label are ignored
                    # during evaluations or not

    'color'       , # The color of this label
    
    'ignoreInTrain',# Whether pixels having this class as ground truth label are ignored

    ] )


#--------------------------------------------------------------------------------
# A list of all labels
#--------------------------------------------------------------------------------

# Please adapt the train IDs as appropriate for you approach.
# Note that you might want to ignore labels with ID 255 during training.
# Further note that the current train IDs are only a suggestion. You can use whatever you like.
# Make sure to provide your results using the original IDs and not the training IDs.
# Note that many IDs are ignored in evaluation and thus you never need to predict these!

labels = [
    #       name                     id    trainId   category            catId     hasInstances   ignoreInEval   color        ignoreInTrain   
    Label(  'unlabeled'            ,  0 ,      0 , 'void'            , 0       , False        , True         , (  10,  50,  30), False),  
    Label(  'ego vehicle'          ,  1 ,      1 , 'void'            , 0       , False        , True         , (  0,  160,  100), False),
    Label(  'rectification border' ,  2 ,      255 , 'void'            , 0       , False        , True         , (  130,  0,  0), True),
    Label(  'out of roi'           ,  3 ,      255 , 'void'            , 0       , False        , True         , (  0,  200,  0), True),
    Label(  'static'               ,  4 ,      255 , 'void'            , 0       , False        , True         , (  10,  100,  53), True),
    Label(  'dynamic'              ,  5 ,      255 , 'void'            , 0       , False        , True         , (111, 74,  0), True),
    Label(  'ground'               ,  6 ,      2 , 'void'            , 0       , False        , True         , ( 81,  0, 81), False),
    Label(  'road'                 ,  7 ,      3 , 'flat'            , 1       , False        , False        , (128, 64,128), False ),
    Label(  'sidewalk'             ,  8 ,      4 , 'flat'            , 1       , False        , False        , (244, 35,232), False ),
    Label(  'parking'              ,  9 ,      5 , 'flat'            , 1       , False        , True         , (250,170,160), False ),
    Label(  'rail track'           , 10 ,      6 , 'flat'            , 1       , False        , True         , (230,150,140), False ),
    Label(  'building'             , 11 ,      7 , 'construction'    , 2       , False        , False        , ( 70, 70, 70), False ),
    Label(  'wall'                 , 12 ,      8 , 'construction'    , 2       , False        , False        , (102,102,156), False ),
    Label(  'fence'                , 13 ,      9 , 'construction'    , 2       , False        , False        , (190,153,153), False ),
    Label(  'guard rail'           , 14 ,      10 , 'construction'    , 2       , False        , True         , (180,165,180), False ),
    Label(  'bridge'               , 15 ,      11 , 'construction'    , 2       , False        , True         , (150,100,100), False ),
    Label(  'tunnel'               , 16 ,      12 , 'construction'    , 2       , False        , True         , (150,120, 90), False ),
    Label(  'pole'                 , 17 ,      13 , 'object'          , 3       , False        , False        , (153,153,153), False ),
    Label(  'polegroup'            , 18 ,      255 , 'object'          , 3       , False        , True         , (153,153,153), True ),
    Label(  'traffic light'        , 19 ,      14 , 'object'          , 3       , False        , False        , (250,170, 30), False ),
    Label(  'traffic sign'         , 20 ,      15 , 'object'          , 3       , False        , False        , (220,220,  0), False ),
    Label(  'vegetation'           , 21 ,      16 , 'nature'          , 4       , False        , False        , (107,142, 35), False ),
    Label(  'terrain'              , 22 ,      17 , 'nature'          , 4       , False        , False        , (152,251,152), False ),
    Label(  'sky'                  , 23 ,      18 , 'sky'             , 5       , False        , False        , ( 70,130,180), False ),
    Label(  'person'               , 24 ,      19 , 'human'           , 6       , True         , False        , (220, 20, 60), False ),
    Label(  'rider'                , 25 ,      20 , 'human'           , 6       , True         , False        , (255,  0,  0), False ),
    Label(  'car'                  , 26 ,      21 , 'vehicle'         , 7       , True         , False        , (  0,  0,142), False ),
    Label(  'truck'                , 27 ,      22 , 'vehicle'         , 7       , True         , False        , (  0,  0, 70), False ),
    Label(  'bus'                  , 28 ,      23 , 'vehicle'         , 7       , True         , False        , (  0, 60,100), False ),
    Label(  'caravan'              , 29 ,      24 , 'vehicle'         , 7       , True         , True         , (  0,  0, 90), False ),
    Label(  'trailer'              , 30 ,      25 , 'vehicle'         , 7       , True         , True         , (  0,  0,110), False ),
    Label(  'train'                , 31 ,      26 , 'vehicle'         , 7       , True         , False        , (  0, 80,100), False ),
    Label(  'motorcycle'           , 32 ,      27 , 'vehicle'         , 7       , True         , False        , (  0,  0,230), False ),
    Label(  'bicycle'              , 33 ,      28 , 'vehicle'         , 7       , True         , False        , (119, 11, 32), False ),
    Label(  'license plate'        , 34 ,      255 , 'vehicle'         , 7       , False        , True         , (  0,  0,142), True ),
]


def get_train_ids():
  train_ids = []
  for i in labels:
    if not i.ignoreInEval:
      train_ids.append(i.id)
  return train_ids