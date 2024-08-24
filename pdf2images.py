import fitz  # PyMuPDF
import argparse
import os


def convert_pdf_to_images(pdf_path, output_dir, image_format='png', resolution=150, image_name='page'):
    """Convert a PDF file to images using PyMuPDF."""
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through each page in the PDF
    for page_number in range(len(pdf_document)):
        # Load a specific page
        page = pdf_document.load_page(page_number)
        # Render page to an image with resolution
        pix = page.get_pixmap(
            matrix=fitz.Matrix(resolution / 72, resolution / 72))

        # Create a filename based on the page number
        output_file = os.path.join(output_dir, f'{image_name}_{page_number + 1}.{image_format}')
        # Save the image
        pix.save(output_file)
        print(f'Saved: {output_file}')

    # Close the PDF document
    pdf_document.close()


def print_banner(banner):
    print(banner)


def init(pdf_path: str, output_dir: str) -> bool:
    if not pdf_path.lower().endswith('.pdf'):
        return False
    if output_dir is None:
        output_dir = os.getcwd() + "./out"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return True


def get_argument_parser(banner):
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="A custom program that converts a PDF file to images(png, jpg, tiff)",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=banner
    )

    # Add arguments
    parser.add_argument(
        'pdf_path',
        help="Path to the PDF file to convert.")
    parser.add_argument(
        'output_dir',
        help="Directory to save the output images. (default: current directory)")
    parser.add_argument(
        '-f',
        '--format',
        default='png',
        choices=['png', 'jpg', 'tiff'],
        help="Output image format (default: png).")
    parser.add_argument(
        '-r',
        '--resolution',
        type=int,
        default=150,
        help="Resolution of the output images in DPI (default: 150).")
    parser.add_argument(
        '-n',
        '--image_name',
        type=str,
        default='page_',
        help="Rename the output images name (default: page_).")

    if '--help' in os.sys.argv or '-h' in os.sys.argv:
        print_banner(banner)

    return parser


def main():
    banner = r"""
    ┌─┐┌┬┐┌─┐┬┌┬┐┌─┐┌─┐┌─┐┌─┐
    ├─┘ ││├┤ ││││├─┤│ ┬├┤ └─┐
    ┴  ─┴┘└  ┴┴ ┴┴ ┴└─┘└─┘└─┘                                        
    
    pdf2images lokcaffee
    """

    parser = get_argument_parser(banner)
    # Parse the arguments
    args = parser.parse_args()

    init(args.pdf_path, args.output_dir)

    # Call the conversion function with the parsed arguments
    convert_pdf_to_images(args.pdf_path, args.output_dir, args.format, args.resolution, args.image_name)


if __name__ == '__main__':
    main()
