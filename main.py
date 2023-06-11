import os
import change_number
import chfont
import merge_video

def add_suffix_to_filepath(filepath, suffix):
    """
    给指定文件路径的文件名添加指定后缀并返回修改后的文件路径
    :param filepath: 文件路径
    :param suffix: 指定的后缀
    :return: 修改后的文件路径
    """
    file_dir, file_name = os.path.split(filepath)
    file_base, file_ext = os.path.splitext(file_name)
    new_name = f"{file_base}_{suffix}{file_ext}"
    new_path = os.path.join(file_dir, new_name)
    return new_path


def remove_change_to_old_name(filename):
    os.remove(filename)
    os.rename(add_suffix_to_filepath(filename,"new"),filename)

def process_files(folder_path):
    """处理指定文件夹下的 mp4 和 srt 文件"""
    for file in os.listdir(folder_path):
        if file.endswith(".mp4"):
            video_file = os.path.join(folder_path, file)
            subtitle_file = os.path.join(folder_path, file[:-3] + "srt")
            if os.path.exists(subtitle_file):
                try:
                    # 执行指定的命令
                    change_number.change_font_number(subtitle_file,add_suffix_to_filepath(subtitle_file,"new"))
                    remove_change_to_old_name(subtitle_file)

                    chfont.change_font(subtitle_file,add_suffix_to_filepath(subtitle_file,"new"))
                    remove_change_to_old_name(subtitle_file)

                    merge_video.add_font(video_file,subtitle_file,add_suffix_to_filepath(video_file,"new"))
                    remove_change_to_old_name(video_file)

                    os.remove(subtitle_file)
                except Exception as e:
                    print(f"执行命令时出错：{e}")
            else:
                print(f"没有找到文件所需的SRT {subtitle_file}")


if __name__ == "__main__":
    process_files("./data")