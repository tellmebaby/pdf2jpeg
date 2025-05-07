# PDF를 JPG로 변환하는 프로그램 (PyMuPDF 사용)
import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path, output_folder, dpi=300):
    """
    PDF 파일을 JPG 이미지로 변환합니다.
    
    :param pdf_path: PDF 파일 경로
    :param output_folder: 이미지가 저장될 폴더 경로
    :param dpi: 이미지 해상도(기본값: 300)
    """
    # 출력 폴더가 없으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # PDF 파일명 추출 (확장자 제외)
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # PDF 파일 열기
    print(f"{pdf_path} 파일 변환 중...")
    pdf_document = fitz.open(pdf_path)
    
    # 픽셀 배율 계산 (DPI/72 - 72는 기본 PDF DPI)
    zoom = dpi / 72
    
    # 각 페이지를 JPG로 저장
    for i, page in enumerate(pdf_document):
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        image_path = os.path.join(output_folder, f"{file_name}_page{i+1}.jpg")
        pix.save(image_path)
        print(f"페이지 {i+1}/{len(pdf_document)} 저장 완료: {image_path}")
    
    print(f"변환 완료! {len(pdf_document)}개의 이미지가 {output_folder}에 저장되었습니다.")

if __name__ == "__main__":
    # 사용자로부터 파일 경로 입력받기
    pdf_path = input("PDF 파일 경로를 입력하세요: ")
    output_folder = input("이미지를 저장할 폴더 경로를 입력하세요: ")
    
    # DPI 설정 (선택사항)
    dpi_input = input("이미지 해상도(DPI)를 입력하세요 (기본값: 300): ")
    dpi = int(dpi_input) if dpi_input else 300
    
    # 변환 실행
    pdf_to_images(pdf_path, output_folder, dpi)