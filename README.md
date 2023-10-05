# AWS Bedrock Demo Script

A simple Python script example showing how to use AWS bedrock via the Python SDK.

To use this you'll first need also need to have the AWS CLI already installed and configured.

You'll also need to enable the Claude, Jurassic and Stability models in your AWS account. These all use
the AWS `us-east-1` region.

## Generate Text Content Using Claude AI

```sh
python generate_text_claude.py
```

Update the `prompt_data` variable to change what it generates.

```python
prompt_data = """
Write a short, 1-sentence 90s horror B-movie pitch
about a giant man-eating Python. Include a bizarre and surprising twist.
"""
```

Example output:

```text
After a scientific experiment goes awry, a giant 20-foot python escapes into the Everglades, devouring tourists and locals alike, until a retired alligator wrestler tries stopping it with the help of his pet chihuahua named Killer.
```

## Generate Text Content Using Jurassic

```sh
python generate_text_j2.py
```

Example output:

```text
"A group of unsuspecting tourists are terrorized by a massive, man-eating Python with a bizarre and surprising twist."
```

## Generate Image Using Stable Diffusion XL

```sh
python generate_image.py
```

Update the `prompt_data` variable to change what it generates.

```python
prompt_data = """
A portrait photo of an dog on a mountain covered in snow in 4k resolution,
award winning photo with HDR lighting, kodak film"
"""
```

They'll be generated to the `output` directory.

Example outputs:

![Puppy Image 1](./puppy_1.png)

![Puppy Image 2](./puppy_2.png)
