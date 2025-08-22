

def copy_static(src_dir, dst_dir):
    import os
    import shutil

    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)

    for entry in os.listdir(src_dir):
        src_path = os.path.join(src_dir, entry)
        dst_path = os.path.join(dst_dir, entry)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            copy_static(src_path, dst_path)
