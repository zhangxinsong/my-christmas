#!/usr/bin/env python3
"""
图片批量压缩脚本
将 images 文件夹中的所有图片压缩到最大 2048px
保持纵横比，使用高质量 JPEG 压缩
"""

import os
import sys
from pathlib import Path
from PIL import Image
import shutil

# 压缩配置（与网页配置保持一致）
MAX_WIDTH = 2048
MAX_HEIGHT = 2048
JPEG_QUALITY = 90
OUTPUT_FORMAT = 'JPEG'

def compress_image(input_path, output_path, backup=True):
    """
    压缩单张图片

    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        backup: 是否备份原图

    Returns:
        dict: 压缩结果信息
    """
    try:
        # 打开图片
        img = Image.open(input_path)

        # 转换RGBA到RGB（处理PNG透明通道）
        if img.mode in ('RGBA', 'LA', 'P'):
            # 创建白色背景
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        original_size = os.path.getsize(input_path)
        original_width, original_height = img.size

        # 检查是否需要缩放
        needs_resize = original_width > MAX_WIDTH or original_height > MAX_HEIGHT

        if needs_resize:
            # 计算新尺寸（保持纵横比）
            aspect_ratio = original_width / original_height

            if aspect_ratio > 1:  # 宽图
                new_width = min(original_width, MAX_WIDTH)
                new_height = round(new_width / aspect_ratio)
            else:  # 高图
                new_height = min(original_height, MAX_HEIGHT)
                new_width = round(new_height * aspect_ratio)

            # 高质量缩放
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        else:
            new_width, new_height = original_width, original_height

        # 备份原图
        if backup and input_path == output_path and (needs_resize or img.format != OUTPUT_FORMAT):
            backup_path = input_path.parent / f"{input_path.stem}_original{input_path.suffix}"
            if not backup_path.exists():
                shutil.copy2(input_path, backup_path)

        # 保存压缩后的图片
        img.save(output_path, OUTPUT_FORMAT, quality=JPEG_QUALITY, optimize=True)

        compressed_size = os.path.getsize(output_path)
        compression_ratio = ((original_size - compressed_size) / original_size * 100) if original_size > 0 else 0

        return {
            'success': True,
            'original_size': original_size,
            'compressed_size': compressed_size,
            'compression_ratio': compression_ratio,
            'original_dimensions': (original_width, original_height),
            'new_dimensions': (new_width, new_height),
            'resized': needs_resize
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def format_size(bytes_size):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} TB"

def compress_folder(folder_path='./images', backup=True, output_folder=None):
    """
    批量压缩文件夹中的所有图片

    Args:
        folder_path: 输入文件夹路径
        backup: 是否备份原图
        output_folder: 输出文件夹（None表示覆盖原图）
    """
    folder = Path(folder_path)
    if not folder.exists():
        print(f"错误: 文件夹 '{folder_path}' 不存在")
        return

    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif'}

    # 收集所有图片文件
    images = [f for f in folder.iterdir()
              if f.is_file() and f.suffix.lower() in image_extensions
              and not f.stem.endswith('_original')]  # 跳过备份文件

    if not images:
        print(f"错误: 在 '{folder_path}' 中没有找到图片文件")
        return

    images.sort()

    print(f"找到 {len(images)} 张图片")
    print(f"压缩配置: 最大尺寸 {MAX_WIDTH}x{MAX_HEIGHT}px, JPEG质量 {JPEG_QUALITY}%")
    print(f"备份模式: {'启用' if backup else '禁用'}")

    if output_folder:
        output_path = Path(output_folder)
        output_path.mkdir(exist_ok=True)
        print(f"输出目录: {output_folder}")
    else:
        print("模式: 覆盖原图")

    print("=" * 70)

    # 统计信息
    success_count = 0
    failed_count = 0
    total_original_size = 0
    total_compressed_size = 0
    resized_count = 0

    # 逐个处理图片
    for i, img_path in enumerate(images, 1):
        # 确定输出路径
        if output_folder:
            # 保存到指定文件夹，统一为.jpg扩展名
            out_path = Path(output_folder) / f"{img_path.stem}.jpg"
        else:
            # 覆盖原图，保持原扩展名或改为.jpg
            out_path = img_path.parent / f"{img_path.stem}.jpg"

        print(f"[{i}/{len(images)}] {img_path.name} ... ", end='', flush=True)

        result = compress_image(img_path, out_path, backup=backup)

        if result['success']:
            success_count += 1
            total_original_size += result['original_size']
            total_compressed_size += result['compressed_size']

            if result['resized']:
                resized_count += 1
                print(f"[OK] {result['original_dimensions'][0]}x{result['original_dimensions'][1]} -> "
                      f"{result['new_dimensions'][0]}x{result['new_dimensions'][1]} "
                      f"({format_size(result['original_size'])} -> {format_size(result['compressed_size'])}, "
                      f"压缩 {result['compression_ratio']:.1f}%)")
            else:
                if result['compression_ratio'] > 0:
                    print(f"[OK] 仅压缩 ({format_size(result['original_size'])} -> "
                          f"{format_size(result['compressed_size'])}, 压缩 {result['compression_ratio']:.1f}%)")
                else:
                    print(f"[OK] 无需处理")
        else:
            failed_count += 1
            print(f"[FAIL] 失败: {result['error']}")

    # 打印总结
    print("=" * 70)
    print(f"完成! 成功: {success_count}, 失败: {failed_count}")
    print(f"调整尺寸: {resized_count} 张")
    print(f"总大小: {format_size(total_original_size)} → {format_size(total_compressed_size)}")

    if total_original_size > 0:
        total_ratio = (total_original_size - total_compressed_size) / total_original_size * 100
        print(f"总压缩率: {total_ratio:.1f}%")
        print(f"节省空间: {format_size(total_original_size - total_compressed_size)}")

if __name__ == '__main__':
    print("=" * 70)
    print("  图片批量压缩工具")
    print("=" * 70)

    # 检查PIL库
    try:
        from PIL import Image
    except ImportError:
        print("\n错误: 缺少 Pillow 库")
        print("请运行: pip install Pillow")
        sys.exit(1)

    # 解析命令行参数
    backup = '--no-backup' not in sys.argv
    output_folder = None

    # 检查是否指定输出文件夹
    for i, arg in enumerate(sys.argv):
        if arg == '--output' or arg == '-o':
            if i + 1 < len(sys.argv):
                output_folder = sys.argv[i + 1]

    compress_folder(folder_path='./images', backup=backup, output_folder=output_folder)

    print("\n提示: 压缩完成后，可以刷新网页查看效果")
    if backup and not output_folder:
        print("原图已备份为 *_original.jpg，确认无误后可删除备份文件")
