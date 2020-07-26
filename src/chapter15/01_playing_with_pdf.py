#! /usr/bin/env python3
# Playing with PDFs

import PyPDF2
import pathlib


def print_first_page_pdf(pdf_reader):
    print(f"Page number: {pdf_reader.numPages}")
    first_page = pdf_reader.getPage(0)
    print(f"{'*' * 20} First Page Content {'*' * 20}")
    print(first_page.extractText())
    print(f"{'*' * 20}********************{'*' * 20}")


# Reading PDF file
pdf_file = pathlib.Path("input_pdf/meetingminutes.pdf")
with open(pdf_file, "rb") as f:
    print(f"Opening '{pdf_file.absolute()}'")
    pdf_reader = PyPDF2.PdfFileReader(f)
    print_first_page_pdf(pdf_reader)

# Reading encrypted PDF file
encrypted_file = pathlib.Path("input_pdf/encrypted.pdf")
with open(encrypted_file, "rb") as f:
    print(f"Opening '{encrypted_file.absolute()}'")
    pdf_reader = PyPDF2.PdfFileReader(f)
    pdf_reader.decrypt("rosebud")
    print_first_page_pdf(pdf_reader)

# Merging two PDF files
with open("input_pdf/meetingminutes.pdf", "rb") as f1, \
        open("input_pdf/meetingminutes2.pdf", "rb") as f2:
    pdf_files = [f1, f2]
    with open("output_pdf/merge_meeting.pdf", "wb") as file_merge:
        pdf_writer = PyPDF2.PdfFileWriter()
        for pdf_file in pdf_files:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for n in range(pdf_reader.numPages):
                page = pdf_reader.getPage(n)
                pdf_writer.addPage(page)
        pdf_writer.write(file_merge)

# Mark all pages
with open("input_pdf/watermark.pdf", "rb") as wf:
    watermark_reader = PyPDF2.PdfFileReader(wf)
    watermark_page = watermark_reader.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    with open("input_pdf/meetingminutes.pdf", "rb") as mf:
        pdf_reader = PyPDF2.PdfFileReader(mf)
        for n in range(pdf_reader.numPages):
            page = pdf_reader.getPage(n)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)
        with open("output_pdf/watermark_meetings.pdf", "wb") as file_watermark_meeting:
            pdf_writer.write(file_watermark_meeting)
