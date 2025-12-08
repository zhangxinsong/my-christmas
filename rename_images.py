#!/usr/bin/env python3
"""
批量重命名图片脚本
将 images 文件夹中的所有图片重命名为 (1).jpg, (2).jpg, (3).jpg ...
"""

import os
import sys
from pathlib import Path

def rename_images(folder_path='./images', output_ext='.jpg', auto_confirm=False):
    """
    批量重命名图片文件

    Args:
        folder_path: 图片文件夹路径
        output_ext: 输出扩展名（.jpg 或 .png）
    """
    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp'}

    # 获取所有图片文件
    folder = Path(folder_path)
    if not folder.exists():
        print(f"错误: 文件夹 '{folder_path}' 不存在")
        return

    # 收集所有图片文件
    images = []
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in image_extensions:
            images.append(file)

    if not images:
        print(f"错误: 在 '{folder_path}' 中没有找到图片文件")
        return

    # 按文件名排序
    images.sort()

    print(f"找到 {len(images)} 张图片")
    print(f"将重命名为: (1){output_ext}, (2){output_ext}, ...")

    # 确认
    if not auto_confirm:
        response = input("是否继续? (y/n): ").strip().lower()
        if response != 'y':
            print("取消操作")
            return
    else:
        print("自动确认模式，开始重命名...")

    # 先重命名为临时名称（避免冲突）
    temp_names = []
    for i, img in enumerate(images, 1):
        temp_name = folder / f"temp_{i}{output_ext}"
        img.rename(temp_name)
        temp_names.append(temp_name)
        print(f"  {img.name} -> temp_{i}{output_ext}")

    # 再重命名为最终名称
    for i, temp_file in enumerate(temp_names, 1):
        final_name = folder / f"({i}){output_ext}"
        temp_file.rename(final_name)
        print(f"  temp_{i}{output_ext} -> ({i}){output_ext}")

    print(f"\n完成! 已重命名 {len(images)} 张图片")
    print(f"\n现在可以将 christmas.html 中的配置修改为:")
    print(f"  autoScanLocal: true,")
    print(f"  scanCount: {len(images)},")
    print(f"  filePattern: '(${{i}})',")
    print(f"  fileExtension: '{output_ext}'")

if __name__ == '__main__':
    print("=" * 50)
    print("  图片批量重命名工具")
    print("=" * 50)

    # 检查命令行参数
    auto_confirm = '--yes' in sys.argv or '-y' in sys.argv

    # 默认使用 .jpg 扩展名
    rename_images(folder_path='./images', output_ext='.jpg', auto_confirm=auto_confirm)
