## Appendix D: Equations

### D.0 Equation Notation and Conventions

This section establishes the mathematical notation, conventions, and semantic interpretations used throughout Appendix D. 

#### D.0.1 Defined As Operator

The symbol `:=` denotes a definition, distinguishing it from a mathematical equality or assertion.

> $x := 5$ means "x is defined as 5"

In "Where:" blocks, `:=` defines or explains the variable.

#### D.0.2 Vector Notation

Vectors are denoted with an arrow above the variable: $\vec{v}$, $\vec{r}$, $\vec{a}$.

This document presents vectors in horizontal or vertical orientations to optimize visual clarity. Vectors appear horizontally as $\vec{v} = [v_x, v_y, v_z]$ or vertically as column vectors based on context and formatting constraints. The orientation choice depends on the mathematical operation and context; vectors should be interpreted in whichever form the surrounding equations require.

> Horizontal representation: 
> $$
> \vec{r}_{\text{ECI}} = [x, y, z]
> $$
>
> Vertical representation:
> $$
> \vec{r}_{\text{ECI}} = \begin{bmatrix} x \\ y \\ z  \end{bmatrix}
> $$
>
> Both represent three-component vectors; the orientation adapts to the surrounding mathematical context.

Unit vectors are denoted with a hat (circumflex) above the variable: $\hat{v} $, $\hat{r} $, $\hat{n} $. A unit vector has magnitude equal to one and indicates direction only.

> $\hat{x} = [1, 0, 0] $ represents a unit vector in the positive X direction

#### D.0.3 Matrix and Quaternion Notation

Direction Cosine Matrices (DCMs) and whole quaternions are denoted with bold typeface to distinguish them as rotation operators rather than scalars or standard vectors.

>  **DCMs**: $\mathbf{R}$, $\mathbf{DCM}$
>
>  **Quaternions**: $\mathbf{Q}$

##### D.0.3.1 DCM Subscripts

DCM subscripts indicate the coordinate frame transformation. The subscript notation reads as `from <source frame> to <destination frame>`.

> $\mathbf{R}_{\text{ECI to ECR}}$ transforms vectors from ECI frame to ECR frame
> $\mathbf{R}_{\text{roll}}(\phi)$ represents a rotation matrix about the roll axis


##### D.0.3.2 Quaternion Subscripts

Quaternion subscripts indicate either the coordinate frame transformation or rotation.


> $\mathbf{Q}_{\text{ECI to ECR}}$ transforms vectors from ECI frame to ECR frame

#### D.0.4 Component Subscripts

Subscript notation identifies individual components of vectors and quaternions.

##### D.0.4.1 Quaternion Component Subscripts

Quaternions consist of one scalar component (s) and three vector components (x,y,z). Quaternions are recorded scalar first.

> $q_s $ : scalar component (also denoted $q_4$ or $q_w$ in some conventions)
> $q_i $ : i-component of vector part (x-direction)
> $q_j $ : j-component of vector part (y-direction)
> $q_k $ : k-component of vector part (z-direction)

Quaternions take the form $\mathbf{Q} = [q_s, q_i, q_j, q_k]$ or $\mathbf{Q} = q_s + q_i\mathbf{i} + q_j\mathbf{j} + q_k\mathbf{k}$.

##### D.0.4.2 Spatial Vector Component Subscripts

Three-dimensional spatial vectors (position, velocity, acceleration) use (x, y, z) subscripts to denote components along coordinate axes.

> $v_x$, $v_y$, $v_z$ : components along X, Y, and Z axes
>
> A complete vector may be written as:
> $$
> \vec{v} = [v_x, v_y, v_z] = \begin{bmatrix} v_x \\ v_y \\ v_z \end{bmatrix}
> $$
> Subscripts often include frame identifiers to clarify the reference frame:
>
> - $\vec{v}_{\text{ECI}} = [v_x, v_y, v_z]$ : velocity vector in ECI frame
> - $\vec{r}_{\text{ECR}} = [r_x, r_y, r_z]$ : position vector in ECR frame

##### D.0.4.3 Frame Transformation Subscripts

Subscripts on rotational quantities (Euler angles, quaternions) follow a naming pattern that indicates the coordinate frame transformation. The subscript syntax derives from the quaternion component field naming in the Trajectory schema.

The general pattern for transformation subscripts in vector components is a minimal version of the Matrix and Quaternion transformation subscript.

> `<source_frame>2<destination_frame>` 
>
> where the numeral `2` serves as shorthand for "to"

This notation specifies the reference frames involved in the rotational transformation:

> $\phi_{\text{I2B}} $ : roll angle transforming from frame I (ECI) to frame B (Body CG)
>
> I2B (Inertial-to-Body, or ECI-to-Body CG) represents the only frame transformation required for quaternions and Euler angles in Appendix D. The I2B pattern corresponds to the ECI to Body CG transformation notation used for DCMs.

#### D.0.5 Mathematical Operators

##### D.0.5.1 Cross Product

The symbol $\times$ denotes the vector cross product.

> $ \vec{c} = \vec{a} \times \vec{b} $

##### D.0.5.2 Multiplication Operator

The symbol $\cdot$ denotes multiplication operations. This operator is shown explicitly for clarity but may be omitted when the operands remain visually distinct. 

> The context (scalar, matrix, or vector operands) determines the specific operation. 
>
> **Scalar multiplication**: 
> $$
> z = x \cdot y = xy
> $$
> **Matrix multiplication**:
> $$
> \mathbf{DCM} = \mathbf{R}_z \cdot \mathbf{R}_y \cdot \mathbf{R}_x = \mathbf{R}_z \mathbf{R}_y\mathbf{R}_x
> $$
> **Matrix-vector multiplication**: 
> $$
> \mathbf{R} \cdot \vec{v} = \mathbf{R}\vec{v}
> $$

##### D.0.5.3 Absolute Value

Single vertical bars $|x|$ denote absolute value of a scalar
$$
x = |-x|
$$


##### D.0.5.4 Magnitude and Norm

Double vertical bars $\| \| $ denote vector normalization or magnitude of a vector, which produces a unit vector by dividing a vector by its magnitude:
$$
\hat{v} = \frac{\vec{v}}{\|\vec{v}\|} = \frac{\vec{v}}{\sqrt{\sum_{i=1}^{n} v_i^2}}
$$
#### D.0.6 Special Functions

##### D.0.6.1 Arctangent Functions

Two arctangent functions appear in this document:

**Single-argument arctangent:** 
$$
\arctan(x)
$$
Returns the angle whose tangent is $x$, with result in the range $(-\pi/2, \pi/2)$.

**Two-argument arctangent:**
$$
\text{arctan2}(y, x)
$$
Returns the angle $\theta$ such that $\tan(\theta) = y/x$, with result in the range $(-\pi, \pi]$. This function accounts for the signs of both arguments to determine the correct quadrant. Usage should be synonymous with `atan2(y,x)` in many programming languages.

##### D.0.6.2 Sign Function

The sign function returns the sign of its argument:

$$
\text{sign}(x) = \begin{cases} 
+1 & \text{if } x > 0 \\ 0 & \text{if } x = 0 \\ -1 & \text{if } x < 0 \end{cases}
$$

#### D.0.7 Unit Conventions

Units appear in square brackets following variable definitions. The International System of Units (SI) and their standard derivatives serve as the default unit system throughout this document.

##### D.0.7.1 Single Unit Notation

When expressing a single unit of measurement, the full word form is used: meters, radians, seconds, kilograms.

>  $r :=$ [meters] radius

##### D.0.7.2 Compound Unit Notation

When expressing compound units (products or quotients of multiple units), shorthand notation is used within the square brackets:

> $\vec{v} :=$ [m/s] velocity vector
> $\omega :=$ [rad/s] angular velocity

#### D.0.8 Data Field References

Field names from the TSEH5 schema are denoted with backticks: `field_name`. This formatting distinguishes data fields from mathematical variables. See [Section 1.5](#1.5 Document Conventions) for complete details.

**Globally Unique Field Names:**

The TSEH5 standard ensures all field names are globally unique across all schemas. Any field can be unambiguously identified by its name alone, without requiring a schema prefix.

**Schema Path Notation:**

Full paths use the pattern `SchemaName.field_name`:
> `SimData.time_0_sim` - simulation initialization time
>
> `Trajectory[i].mass` - mass at trajectory point i  
>
> `SMHR.name_threat` - threat name from SMHR schema

**Abbreviated Notation in Appendix D:**

Due to global field uniqueness, this appendix frequently omits `Trajectory` schema prefixes for conciseness, since most fields referenced in coordinate transformations originate from the `Trajectory` schema. The array index `[i]` is also typically omitted since equations describe transformations at individual trajectory states. 

> `time` → `Trajectory[i].time`
>
> `mass` → `Trajectory[i].mass`
>
> `x_pos_eci` → `Trajectory[i].x_pos_eci`


#### D.0.9 Section Cross-References

Internal cross-references to other sections within this document use the format:

```
identifier := link
```

This indicates that the identifier is defined elsewhere in Appendix D.

#### D.0.10 Variable Definition Blocks

Equations are followed by "Where:" blocks that define the variables, parameters, and symbols used in the equation. These blocks follow a consistent structure:

```
Where:

- identifier := [units] description reference to TSEH5 field
```

Each line in a "Where:" block provides:

1. **Variable**: The mathematical symbol used in the equation
2. **Definition operator**: `:=` indicating the variable is being defined
3. **Units**: Physical units in square brackets, if applicable
4. **Description**: Brief explanation of the variable's meaning, often including:
   - Physical interpretation
   - Source (TSEH5 field reference using backticks)
   - Valid ranges or constraints
   - Cross-references to other sections

___

### D.1 Rotational State Transformations

#### D.1.1 DCM Rotations

##### D.1.1.1 Roll Rotation Matrix

This matrix rotates vectors about the X-axis by angle φ, transforming coordinates in the YZ-plane while leaving the X-component unchanged.
$$
\mathbf{R}_{\text{roll}}(\phi) = \begin{bmatrix}1 & 0 & 0 \\0 & \cos(\phi) & \sin(\phi) \\0 & -\sin(\phi) & \cos(\phi)\end{bmatrix}
$$

Where:
- $\mathbf{R}_{\text{roll}}(\phi) := $ Roll Rotation Matrix
- $\phi := $ Roll angle (rotation about X-axis)

##### D.1.1.2 Pitch Rotation Matrix

This matrix rotates vectors about the Y-axis by angle θ, transforming coordinates in the XZ-plane while leaving the Y-component unchanged.
$$
\mathbf{R}_{\text{pitch}}(\theta) = \begin{bmatrix}
\cos(\theta) & 0 & -\sin(\theta) \\
0 & 1 & 0 \\
\sin(\theta) & 0 & \cos(\theta)
\end{bmatrix}
$$

Where:
- $\mathbf{R}_{\text{pitch}}(\theta) := $ Pitch Rotation Matrix
- $\theta := $ pitch angle (rotation about Y-axis)

##### D.1.1.3 Yaw Rotation Matrix

This matrix rotates vectors about the Z-axis by angle ψ, transforming coordinates in the XY-plane while leaving the Z-component unchanged.
$$
\mathbf{R}_{\text{yaw}}(\psi) = \begin{bmatrix}
\cos(\psi) & \sin(\psi) & 0 \\
-\sin(\psi) & \cos(\psi) & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Where:
- $\mathbf{R}_{\text{yaw}}(\psi) := $ Yaw Rotation Matrix
- $\psi := $ yaw angle (rotation about Z-axis)

##### D.1.1.4 Yaw-Pitch-Roll Rotation Sequence DCM

All rotation sequences in this document apply yaw-pitch-roll order.

###### D.1.1.4.1 Composite DCM

The full rotation matrix for a yaw-pitch-roll sequence is formed by multiplying the individual rotation matrices:
$$
\mathbf{DCM}(\phi, \theta, \psi) = \mathbf{R}_{\text{roll}}(\phi) \cdot \mathbf{R}_{\text{pitch}}(\theta) \cdot  \mathbf{R}_{\text{yaw}}(\psi)
$$

Where:

- $\mathbf{DCM}(\phi, \theta, \psi) := $ direction cosine matrix for Yaw-Pitch-Roll rotation sequence
- $\mathbf{R}_{\text{roll}}(\phi) := $ [Roll Rotation Matrix](#D.1.1.1 Roll Rotation Matrix)
- $\mathbf{R}_{\text{pitch}}(\theta) := $ [Pitch Rotation Matrix](#D.1.1.2 Pitch Rotation Matrix)
- $\mathbf{R}_{\text{yaw}}(\psi) := $ [Yaw Rotation Matrix](#D.1.1.3 Yaw Rotation Matrix)

###### D.1.1.4.2 Expanded Form

Expanding the matrix multiplication yields the following form in terms of all three Euler angles:
$$
\scriptsize{\mathbf{DCM}(\phi, \theta, \psi) = \begin{bmatrix}
\cos(\theta)\cos(\psi) & \cos(\theta)\sin(\psi) & -\sin(\theta) \\
-\cos(\phi)\sin(\psi) + \sin(\phi)\sin(\theta)\cos(\psi) & \cos(\phi)\cos(\psi) + \sin(\phi)\sin(\theta)\sin(\psi) & \sin(\phi)\cos(\theta) \\
\sin(\phi)\sin(\psi) + \cos(\phi)\sin(\theta)\cos(\psi) & -\sin(\phi)\cos(\psi) + \cos(\phi)\sin(\theta)\sin(\psi) & \cos(\phi)\cos(\theta)
\end{bmatrix}}
$$

Where:
- $\mathbf{DCM}(\phi, \theta, \psi) := $ direction cosine matrix for Yaw-Pitch-Roll rotation sequence
- $\phi := $ roll angle (rotation about X-axis)
- $\theta := $ pitch angle (rotation about Y-axis)
- $\psi := $ yaw angle (rotation about Z-axis)

#### D.1.2 Quaternions and Euler Angles

Conversions between quaternion and Euler angle rotation representations follow the yaw-pitch-roll sequence convention.

##### D.1.2.1 Quaternion to Euler Angles

These equations extract roll, pitch, and yaw Euler angles from quaternion components.

$$
\begin{aligned}
\phi &= \text{arctan2}(2(q_s q_i + q_j q_k), (q_s^2 - q_i^2 - q_j^2 + q_k^2)) \\
\theta &= \arcsin (2(q_s q_j - q_k q_i)) \\
\psi &= \text{arctan2}(2(q_s q_k + q_i q_j), (q_s^2 + q_i^2 - q_j^2 - q_k^2))
\end{aligned}
$$
Where:

- $\phi $ := [radians] roll angle
- $\theta $ := [radians] pitch angle
- $\psi $ := [radians] yaw angle
- $q_s $ := `qs_i2b` (scalar component)
- $q_i $ := `qi_i2b` (i component)
- $q_j $ := `qj_i2b` (j component)
- $q_k $ := `qk_i2b` (k component)

##### D.1.2.2 Euler Angles to Quaternion

These equations convert roll, pitch, and yaw Euler angles into the four quaternion components.
$$
\begin{aligned}
q_s &= \cos(\psi/2)\cos(\theta/2)\cos(\phi/2) + \sin(\psi/2)\sin(\theta/2)\sin(\phi/2) \\
q_i &= \cos(\psi/2)\cos(\theta/2)\sin(\phi/2) - \sin(\psi/2)\sin(\theta/2)\cos(\phi/2) \\
q_j &= \cos(\psi/2)\sin(\theta/2)\cos(\phi/2) + \sin(\psi/2)\cos(\theta/2)\sin(\phi/2) \\
q_k &= \sin(\psi/2)\cos(\theta/2)\cos(\phi/2) - \cos(\psi/2)\sin(\theta/2)\sin(\phi/2) 
\end{aligned}
$$

Where:
- $q_s $ := `qs_i2b` (scalar component)
- $q_i $ := `qi_i2b` (i component)
- $q_j $ := `qj_i2b` (j component)
- $q_k $ := `qk_i2b` (k component)
- $\phi $ := [radians] roll angle
- $\theta $ := [radians] pitch angle
- $\psi $ := [radians] yaw angle


> This conversion assumes a yaw-pitch-roll rotation sequence, consistent with the rotation sequence used throughout this document.

##### D.1.2.3 Quaternion to Body Direction Vector

The x-body unit vector represents the missile's longitudinal axis direction in the reference frame. It corresponds to the first row of the rotation matrix derived from the quaternion.

$$
\vec{x}_{\text{body}} = \begin{bmatrix} 
1 - 2(q_j^2 + q_k^2) \\ 
2(q_i q_j + q_s q_k) \\
2(q_i q_k - q_s q_j) 
\end{bmatrix}
$$

Where:

- $\vec{x}_{\text{body}} $ := body direction unit vector in reference frame [x, y, z]
- $q_s $ := `qs_i2b` (scalar component)
- $q_i $ := `qi_i2b` (i component)
- $q_j $ := `qj_i2b` (j component)
- $q_k $ := `qk_i2b` (k component)

___

### D.2 Spatial State Transformations

The flow chart shows conversion paths between coordinate frames. This appendix provides equations only for frame pairs connected in the flow chart.

> For example, converting between ECI and NED frame requires the following path:
>
> ECI → ECR → ENU → NED

LLA transformations apply to position only.

![CoordinateFrameFlow](.\reference\imgs\CoordinateFrameFlow_Frame.png)
