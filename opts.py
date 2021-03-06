import argparse
import os
def parse_opt():
    # Hyper Parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, default='nlp_cross')
    parser.add_argument('--data_path', default='data', help='path to datasets')
    parser.add_argument('--data_name', default='coco_precomp', help='{coco,f8k,f30k,10crop}_precomp|coco|f8k|f30k')
    parser.add_argument('--vocab_path', default='./vocab/', help='Path to saved vocabulary pickle files.')
    parser.add_argument('--margin', default=0.05, type=float, help='Rank loss margin.')
    parser.add_argument('--num_epochs', default=30, type=int, help='Number of training epochs.')
    parser.add_argument('--batch_size', default=2, type=int, help='Size of a training mini-batch.')
    # CNN
    parser.add_argument('--text_enc_init', default=0, type=int)
    # RNN
    parser.add_argument('--rnn_type', default='GRU', type=str)
    parser.add_argument('--word_dim', default=300, type=int, help='Dimensionality of the word embedding.')
    parser.add_argument('--embed_size', default=1024, type=int, help='Dimensionality of the joint embedding.')
    parser.add_argument('--grad_clip', default=2., type=float, help='Gradient clipping threshold.')
    parser.add_argument('--crop_size', default=224, type=int, help='Size of an image crop as the CNN input.')
    parser.add_argument('--num_layers', default=1, type=int, help='Number of GRU layers.')
    parser.add_argument('--drop_prob_lm', type=float, default=0.5)
    # Optimization
    parser.add_argument('--learning_rate', default=.0002, type=float, help='Initial learning rate.')
    parser.add_argument('--lr_update', default=15, type=int, help='Number of epochs to update the learning rate.')
    parser.add_argument('--workers', default=10, type=int, help='Number of data loader workers.')
    parser.add_argument('--log_step', default=10, type=int, help='Number of steps to print and record the log.')
    parser.add_argument('--val_step', default=500, type=int, help='Number of steps to run validation.')
    parser.add_argument('--logger_name', default='runs/nlp_cross', help='Path to save the model and Tensorboard log.')
    parser.add_argument('--resume', default='', type=str, metavar='PATH', help='path to latest checkpoint (default: none)')
    parser.add_argument('--max_violation', action='store_true', help='Use max instead of sum in the rank loss.')
    parser.add_argument('--img_dim', default=4096, type=int, help='Dimensionality of the image embedding.')
    parser.add_argument('--finetune', action='store_true', help='Fine-tune the image encoder.')
    parser.add_argument('--cnn_type', default='resnet152', help="""The CNN used for image encoder (e.g. vgg19, resnet152)""")
    parser.add_argument('--use_restval', action='store_true', help='Use the restval data for training on MSCOCO.')
    parser.add_argument('--measure', default='cosine', help='Similarity measure used (cosine|order)')
    parser.add_argument('--use_abs', action='store_true', help='Take the absolute value of embedding vectors.')
    parser.add_argument('--no_imgnorm', action='store_true', help='Do not normalize the image embeddings.')
    opt = parser.parse_args()
    print(opt)

    return opt
