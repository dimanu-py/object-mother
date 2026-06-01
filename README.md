# Sindri: Object Mother

### Object Mother pattern for Python test data generation

Easy use and customizable implementation for the Object Mother pattern.

<p align="center">
  <a href="https://dimanu-py.github.io/sindri/getting_started/">Getting Started</a>&nbsp;&nbsp;•&nbsp;
  <a href="https://dimanu-py.github.io/sindri/object_mothers/">Object Mother Pattern</a>
</p>

<div align="center"><table><tr><td>
Sindri object mother replaces ad hoc test data with a consistent Object Mother toolkit.
Generate realistic test data for your domain objects with a simple and focused API.

<br>

<b>Why use it?</b> Generating test data with Sindri lets you:

<ul style="list-style-type: none">
  <li>🧪 Generate business-related test data via the Object Mother pattern</li>
  <li>🧰 Start from ready-made mothers for primitives and identifiers</li>
  <li>🧩 Compose complex test data by combining multiple mothers</li>
  <li>🔄 Reproduce test scenarios with seeded random data</li>
</ul>

</td></tr></table></div>

<div style="background-color: #1e2d3d; border: 1px solid #00d9ff; border-radius: 8px; padding: 16px; margin: 16px 0; display: flex; align-items: flex-start; gap: 12px;">
  <div style="font-size: 20px; color: #00d9ff; flex-shrink: 0;">💧</div>
  <div>
    <strong style="color: #00d9ff;">Created with Instant Python</strong><br>
    <span style="color: #a0a0a0;">This project was generated using <a href="https://github.com/dimanu-py/instant-python" style="color: #00d9ff; text-decoration: none;">Instant Python</a>, a fast, easy and reliable project generator for Python projects.</span>
  </div>
</div>

## Fast Kickstart

```bash
pip install object-mother-sindri      # includes faker for test data
```

Generate random test data for your tests:

```python
from object_mother import IntegerPrimitivesMother, StringPrimitivesMother

random_age = IntegerPrimitivesMother.any()
random_name = StringPrimitivesMother.any()
```

## Next Steps

- [Installation](https://dimanu-py.github.io/sindri/getting_started/installation/)
- [First Steps](https://dimanu-py.github.io/sindri/getting_started/first_steps/)
- [Object Mother Pattern](https://dimanu-py.github.io/sindri/object_mothers/)
- [Contributing Guide](https://dimanu-py.github.io/sindri/contributing/contributing_guide/)

<div style="background-color: #1e2d3d; border: 1px solid #00d9ff; border-radius: 8px; padding: 16px; margin: 16px 0; display: flex; align-items: flex-start; gap: 12px;">
  <div style="font-size: 20px; color: #00d9ff; flex-shrink: 0;">ℹ️</div>
  <div>
    <strong style="color: #00d9ff;">Learn More</strong><br>
    <span style="color: #a0a0a0;">To learn more about the object mother pattern, built-in mothers, and how to create custom mothers, visit the <a href="https://dimanu-py.github.io/sindri/object_mothers" style="color: #00d9ff; text-decoration: none;">Object Mother Pattern</a> section of the documentation.</span>
  </div>
</div>
