from PIL import Image

from main import generate_qr_code, is_valid_url


def test_url_validation():
    assert is_valid_url("https://www.njit.edu")
    assert not is_valid_url("not-a-url")


def test_generates_valid_png(tmp_path):
    output = tmp_path / "qr.png"

    generate_qr_code("https://www.njit.edu", output)

    assert output.exists()
    with Image.open(output) as image:
        assert image.format == "PNG"
        image.verify()


def test_invalid_url_creates_no_image(tmp_path):
    output = tmp_path / "qr.png"

    generate_qr_code("not-a-url", output)

    assert not output.exists()
