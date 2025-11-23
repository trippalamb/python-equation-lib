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

___

#### D.2.0 Common Earth Dynamics

This section defines Earth rotation parameters used in coordinate transformations between inertial (ECI) and rotating (ECR) reference frames.

##### D.2.0.1 Earth Angular Velocity

Earth angular velocity represents the rate of rotation of Earth about its polar axis. This fundamental constant is defined in the World Geodetic System 1984 (WGS84) reference model.

**WGS84 Standard Value:**
$$
\omega_{\text{Earth}} = 7.292115 \times 10^{-5} \text{ rad/s}
$$

The vector form expresses the rotation about the Z-axis (polar axis):

$$
\vec{\Omega}_{\text{Earth}} = \begin{bmatrix} 0 \\ 0 \\ \omega_{\text{Earth}} \end{bmatrix} \text{ rad/s}
$$

Where:

- $\omega_{\text{Earth}} :=$ [rad/s] Earth angular velocity magnitude
- $\vec{\Omega}_{\text{Earth}} :=$ [rad/s] Earth angular velocity vector in ECI and ECR frames

##### D.2.0.2 Earth Rotation Angle

The Earth rotation angle represents the angular displacement of Earth about its rotation axis since the simulation initialization time. This angle quantifies the relative orientation between ECI and ECR reference frames at any given trajectory time.

> At `t = 0`, the angle is zero, meaning ECI and ECR frames are aligned. As time progresses, Earth rotates within the ECR frame while the ECI frame remains inertially fixed, causing the frames to become progressively misaligned.

$$
\psi_{\text{Earth}} = \omega_{\text{Earth}} \cdot t
$$

Where:

- $\psi_{\text{Earth}} :=$ [radians] Earth rotation angle since simulation initialization
- $\omega_{\text{Earth}} :=$ [rad/s] [Earth angular velocity magnitude](#D.2.0.1 Earth Angular Velocity)
- $t :=$ [seconds] current trajectory time: `Trajectory[i].time`

##### D.2.0.3 Transport Velocity

Transport velocity represents the velocity component induced by Earth's rotation at a given position in the ECR frame. Objects stationary in the ECR frame possess this transport velocity when observed from the ECI frame due to their motion with Earth's rotation. The magnitude of transport velocity increases linearly with distance from Earth's rotation axis.

$$
\vec{v}_{\text{transport}} = \vec{\Omega}_{\text{Earth}} \times \vec{r}_{\text{ECI}}
$$

Where:

- $\vec{v}_{\text{transport}} :=$ [m/s] transport velocity vector in ECI frame
- $\vec{\Omega}_{\text{Earth}} :=$ [rad/s] [Earth angular velocity vector](#D.2.0.1 Earth Angular Velocity)
- $\vec{r}_{\text{ECI}} :=$ [meters] position vector in ECI frame: [`x_pos_eci`, `y_pos_eci`, `z_pos_eci`]

##### D.2.0.4 Relative Velocity (ECI)

Relative velocity in ECI represents the velocity of an object relative to Earth's rotating surface, with vector components expressed in the inertial ECI frame. This quantity isolates the object's motion with respect to the ground from the motion induced by Earth's rotation.
$$
\vec{v}_{\text{relative, ECI}} = \vec{v}_{\text{ECI}} - \vec{v}_{\text{transport}}
$$

Where:

- $\vec{v}_{\text{relative, ECI}} :=$ [m/s] relative velocity vector in ECI frame
- $\vec{v}_{\text{ECI}} :=$ [m/s] velocity vector in ECI frame: [`x_vel_eci`, `y_vel_eci`, `z_vel_eci`]
- $\vec{v}_{\text{transport}} :=$ [m/s] [transport velocity](#D.2.0.3 Transport Velocity)



##### D.2.0.5 Coriolis Acceleration

Coriolis acceleration is an apparent acceleration observed in rotating frames, arising from the motion of an object relative to the rotating frame. This term appears in acceleration transformations between ECI and ECR frames.

$$
\vec{a}_{\text{Coriolis}} = 2 \cdot (\vec{\Omega}_{\text{Earth}} \times \vec{v}_{\text{relative, ECI}})
$$

Where:

- $\vec{a}_{\text{Coriolis}} :=$ [m/s²] Coriolis acceleration vector in ECI frame
- $\vec{\Omega}_{\text{Earth}} :=$ [rad/s] [Earth angular velocity vector](#D.2.0.1 Earth Angular Velocity)
- $\vec{v}_{\text{relative, ECI}} := $ [m/s] [relative velocity vector in ECI frame](#D.2.0.4 Relative Velocity (ECI))

##### D.2.0.6 Centripetal Acceleration

Centripetal acceleration represents the acceleration directed toward Earth's rotation axis required to maintain circular motion at a given position in the rotating ECR frame. This term accounts for the time rate of change of transport velocity.

$$
\vec{a}_{\text{centripetal}} = \vec{\Omega}_{\text{Earth}} \times \vec{v}_{\text{transport}}
$$

Where:

- $\vec{a}_{\text{centripetal}} :=$ [m/s²] centripetal acceleration vector in ECI frame
- $\vec{\Omega}_{\text{Earth}} :=$ [rad/s] [Earth angular velocity vector](#D.2.0.1 Earth Angular Velocity)
- $\vec{v}_{\text{transport}} :=$ [m/s] [transport velocity](#D.2.0.3 Transport Velocity)

##### D.2.0.7 Relative Acceleration (ECI)

Relative acceleration in ECI represents the acceleration of an object as observed in Earth's rotating frame, with vector components expressed in the inertial ECI frame. This transformation removes the inertial forces (Coriolis and centripetal) that appear when observing motion from a rotating reference frame.
$$
\vec{a}_{\text{relative, ECI}} = \vec{a}_{\text{ECI}} - \vec{a}_{\text{Coriolis}} - \vec{a}_{\text{centripetal}}
$$

Where:

- $\vec{a}_{\text{relative, ECI}} :=$ [m/s²] relative acceleration vector in ECI frame
- $\vec{a}_{\text{ECI}} :=$ [m/s²] acceleration vector in ECI frame: [`x_acc_eci`, `y_acc_eci`, `z_acc_eci`]
- $\vec{a}_{\text{Coriolis}} :=$ [m/s²] [Coriolis acceleration](#D.2.0.5 Coriolis Acceleration)
- $\vec{a}_{\text{centripetal}} :=$ [m/s²] [centripetal acceleration](#D.2.0.6 Centripetal Acceleration)

---

#### D.2.1 From ECI

This section defines equations that transform spatial states from ECI frame to other reference frames.

##### D.2.1.1 ECI To ECR

The ECI to ECR transformation accounts for Earth's rotation, requiring corrections for transport velocity in velocity transformations and additional Coriolis and centripetal acceleration terms in acceleration transformations.

###### D.2.1.1.1 ECI to ECR (DCM)

The direction cosine matrix for ECI to ECR transformation consists of a rotation about the Z-axis by Earth's rotation angle since simulation initialization.
$$
\begin{aligned}
\mathbf{R}_{\text{ECI to ECR}} = \mathbf{R}_{\text{ECI to ECR}}(\psi_{\text{Earth}}) &= \mathbf{R}_{\text{yaw}}(\psi_{\text{Earth}})
\end{aligned}
$$

Where:

- $\mathbf{R}_{\text{ECI to ECR}} :=$ direction cosine matrix transforming from ECI to ECR frame

- $\mathbf{R}_{\text{yaw}} :=$ [Yaw rotation matrix](#D.1.1.3 Yaw Rotation Matrix)

- $\psi_{\text{Earth}} :=$  [radians] [Earth rotation angle](#D.2.0.2 Earth Rotation Angle) since simulation initialization

  

###### D.2.1.1.2 ECI to ECR Position

Position transformation between ECI and ECR frames requires only rotation, as both frames share the same origin at Earth's center of mass.
$$
\vec{r}_{\text{ECR}} = \mathbf{R}_{\text{ECI to ECR}} \cdot \vec{r}_{\text{ECI}}
$$

Where:

- $\vec{r}_{\text{ECR}} :=$ [meters] position vector in ECR frame
- $\vec{r}_{\text{ECI}} :=$ [meters] position vector in ECI frame: [`x_pos_eci`, `y_pos_eci`, `z_pos_eci`]
- $\mathbf{R}_{\text{ECI to ECR}} :=$ [ECI to ECR DCM](#D.2.1.1.1 ECI to ECR (DCM))

###### D.2.1.1.3 ECI to ECR Velocity

Velocity transformation from ECI to ECR accounts for the transport velocity induced by Earth's rotation and rotates the velocity vector into the ECR frame basis. This transformation uses [relative velocity](#D.2.0.4 Relative Velocity (ECI)) to simplify the equation.
$$
\begin{aligned}
\vec{v}_{\text{ECR}} &= \mathbf{R}_{\text{ECI to ECR}} \cdot \vec{v}_{\text{relative, ECI}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{ECR}} :=$ [m/s] velocity vector in ECR frame
- $\mathbf{R}_{\text{ECI to ECR}} :=$ [ECI to ECR DCM](#D.2.1.1.1 ECI to ECR (DCM))
- $\vec{v}_{\text{relative, ECI}} := $ [m/s] [relative velocity vector in ECI frame](#D.2.0.4 Relative Velocity (ECI))

###### D.2.1.1.4 ECI to ECR Acceleration

Acceleration transformation from ECI to ECR accounts for the Coriolis and centripetal accelerations that arise in rotating reference frames and rotates the acceleration vector into the ECR frame basis. This transformation uses [relative acceleration](#D.2.0.7 Relative Acceleration (ECI)) to simplify the equation.
$$
\begin{aligned}
  \vec{a}_{\text{ECR}} &= \mathbf{R}_{\text{ECI to ECR}} \cdot \vec{a}_{\text{relative, ECI}}
  \end{aligned}
$$

  

Where:

- $\vec{a}_{\text{ECR}} :=$ [m/s²] acceleration vector in ECR frame
- $\mathbf{R}_{\text{ECI to ECR}} :=$ [ECI to ECR DCM](#D.2.1.1.1 ECI to ECR (DCM))
- $\vec{a}_{\text{relative, ECI}} :=$ [m/s²] [relative acceleration in ECI frame](#D.2.0.7 Relative Acceleration (ECI))

##### D.2.1.2 ECI To Body CG

The ECI to Body CG transformation rotates vectors from the inertial reference frame to the body frame centered at the missile's center of gravity.

###### D.2.1.2.1 ECI to Body CG (DCM)

The direction cosine matrix transforming from ECI to Body CG frame is the Yaw-Pitch-Roll DCM constructed from Euler angles obtained through quaternion conversion.
$$
\mathbf{R}_{\text{ECI to BodyCG}} = \mathbf{R}_{\text{ECI to BodyCG}}(\phi_{\text{I2B}}, \theta_{\text{I2B}}, \psi_{\text{I2B}}) = \mathbf{DCM}(\phi, \theta, \psi)
$$

Where:

- $\mathbf{R}_{\text{ECI to BodyCG}} :=$ direction cosine matrix transforming from ECI to Body CG frame
- $\mathbf{DCM}(\phi, \theta, \psi) := $ [Yaw-Pitch-Roll DCM](#D.1.1.4 Yaw-Pitch-Roll Rotation Sequence DCM)
- $\phi_{\text{I2B}} := $ roll rotation from ECI to Body CG frame: [derived](#D.1.2.1 Quaternion to Euler Angles) from `q*_i2b` fields.
- $\theta_{\text{I2B}} :=$ pitch rotation from ECI to Body CG frame: [derived](#D.1.2.1 Quaternion to Euler Angles) from `q*_i2b` fields.
- $\psi_{\text{I2B}} := $ yaw rotation from ECI to Body CG frame: [derived](#D.1.2.1 Quaternion to Euler Angles) from `q*_i2b` fields.

###### D.2.1.2.2 ECI to Body CG Position

The missile's position in its own body frame is always at the origin: $[0, 0, 0]$.
$$
\vec{r}_{\text{BodyCG}} = [0, 0, 0]
$$

Where:

- $\vec{r}_{\text{BodyCG}} :=$ [meters] position vector in Body CG frame

###### D.2.1.2.3 ECI to Body CG Velocity and Acceleration

Velocity and acceleration vectors transform from ECI to Body CG frame through rotation only, as both velocity and acceleration are defined at the center of gravity.
$$
\begin{aligned}
\vec{v}_{\text{BodyCG}} &= \mathbf{R}_{\text{ECI to BodyCG}} \cdot \vec{v}_{\text{ECI}} \\
\vec{a}_{\text{BodyCG}} &= \mathbf{R}_{\text{ECI to BodyCG}} \cdot \vec{a}_{\text{ECI}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{BodyCG}} :=$ [m/s] velocity vector in Body CG frame
- $\vec{a}_{\text{BodyCG}} :=$ [m/s²] acceleration vector in Body CG frame
- $\mathbf{R}_{\text{ECI to BodyCG}} :=$ [ECI to Body CG DCM](#D.2.1.2.1 ECI to Body CG (DCM))
- $\vec{v}_{\text{ECI}} :=$ [m/s] velocity vector in ECI frame: [`x_vel_eci`, `y_vel_eci`, `z_vel_eci`]
- $\vec{a}_{\text{ECI}} :=$ [m/s²] acceleration vector in ECI frame: [`x_acc_eci`, `y_acc_eci`, `z_acc_eci`]

#### D.2.2 From ECR

This section defines equations that transform spatial states from ECR frame to other reference frames.

##### D.2.2.1 ECR to ECI

The ECR to ECI transformation is the inverse of the ECI to ECR transformation, accounting for Earth's rotation by adding transport velocity and fictitious acceleration terms.

###### D.2.2.1.1 ECR to ECI (DCM)

The ECR to ECI transformation is the inverse of the ECI to ECR transformation. Since rotation matrices are orthogonal, the inverse equals the transpose.
$$
\mathbf{R}_{\text{ECR to ECI}} = \mathbf{R}_{\text{ECR to ECI}}(\psi_{\text{Earth}}) = \mathbf{R}_{\text{ECI to ECR}}^T(\psi_{\text{Earth}})
$$

Where:

- $\mathbf{R}_{\text{ECR to ECI}} :=$ direction cosine matrix transforming from ECR to ECI frame
- $\mathbf{R}_{\text{ECI to ECR}}^T :=$ transpose of [ECI to ECR DCM](#D.2.1.1.1 ECI to ECR (DCM))

###### D.2.2.1.2 ECR to ECI Position

Position transformation between ECR and ECI frames requires only rotation, as both frames share the same origin at Earth's center of mass.
$$
\vec{r}_{\text{ECI}} = \mathbf{R}_{\text{ECR to ECI}} \cdot \vec{r}_{\text{ECR}}
$$

Where:

- $\vec{r}_{\text{ECI}} :=$ [meters] position vector in ECI frame: [`x_pos_eci`, `y_pos_eci`, `z_pos_eci`]
- $\vec{r}_{\text{ECR}} :=$ [meters] [position vector in ECR frame](#D.2.1.1.2 ECI to ECR Position)
- $\mathbf{R}_{\text{ECR to ECI}} :=$ [ECR to ECI DCM](#D.2.2.1.1 ECR to ECI (DCM))

###### D.2.2.1.3 ECR to ECI Velocity

Velocity transformation from ECR to ECI rotates the velocity vector into the inertial frame basis and adds the transport velocity component induced by Earth's rotation, recovering the full inertial velocity.
$$
\begin{aligned}
\vec{v}_{\text{ECI}} &= \mathbf{R}_{\text{ECR to ECI}} \cdot \vec{v}_{\text{ECR}} + \vec{v}_{\text{transport}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{ECI}} :=$ [m/s] velocity vector in ECI frame: [`x_vel_eci`, `y_vel_eci`, `z_vel_eci`]
- $\mathbf{R}_{\text{ECR to ECI}} :=$ [ECR to ECI DCM](#D.2.2.1.1 ECR to ECI (DCM))
- $\vec{v}_{\text{ECR}} :=$ [m/s] [velocity vector in ECR frame](#D.2.1.1.3 ECI to ECR Velocity)
- $\vec{v}_{\text{transport}} :=$ [m/s] [transport velocity](#D.2.0.3 Transport Velocity)

###### D.2.2.1.4 ECR to ECI Acceleration

Acceleration transformation from ECR to ECI rotates the acceleration vector into the inertial frame basis and adds the Coriolis and centripetal acceleration terms that arise in rotating reference frames, recovering the full inertial acceleration.
$$
\begin{aligned}
\vec{a}_{\text{ECI}} &= \mathbf{R}_{\text{ECR to ECI}} \cdot \vec{a}_{\text{ECR}} + \vec{a}_{\text{Coriolis}} + \vec{a}_{\text{centripetal}}
\end{aligned}
$$



Where:

- $\vec{a}_{\text{ECI}} :=$ [m/s²] acceleration vector in ECI frame: [`x_acc_eci`, `y_acc_eci`, `z_acc_eci`]
- $\mathbf{R}_{\text{ECR to ECI}} :=$ [ECR to ECI DCM](#D.2.2.1.1 ECR to ECI (DCM))
- $\vec{a}_{\text{ECR}} :=$ [m/s²] [acceleration vector in ECR frame](#D.2.1.1.4 ECI to ECR Acceleration)
- $\vec{a}_{\text{Coriolis}} :=$ [m/s²] [Coriolis acceleration](#D.2.0.5 Coriolis Acceleration)
- $\vec{a}_{\text{centripetal}} :=$ [m/s²] [centripetal acceleration](#D.2.0.6 Centripetal Acceleration)

##### D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA)

Conversion from ECR Cartesian coordinates to geodetic latitude, longitude, and altitude uses an iterative algorithm that accounts for Earth's ellipsoidal shape.

> **Reference:** [.\reference\docs\AccurateEcefConversion-31oct2019.pdf](#A.1 Accurate Conversion of Earth-Fixed Earth-Centered Coordinates to Geodetic Coordinates)

$$
\small{\begin{aligned}
w &= \sqrt{{\vec{r}_{\text{x,ECR}}}^2 + {\vec{r}_{\text{y,ECR}}}^2} \\ \\
l &= \varepsilon^2/2 \\ \\
m &= w^2/r_a^2 \\ \\
n &= {\vec{r}_{\text{z,ECR}}}^2(1-\varepsilon^2)/r_a^2 \\ \\
p &= (m + n - 4l^2)/6 \\ \\
G &= mnl^2 \\ \\
H &= 2p^3 + G \\ \\
\text{if } (H < H_{\min}) &\text{ then abort} \\ \\
C &= \frac{\sqrt[3]{H + G + 2\sqrt{HG}}}{\sqrt[3]{2}} \\ \\
i &= -(2l^2 + m + n)/2 \\ \\
\beta &= i/3 - C - p^2/C \\ \\
k &= l^2(l^2 - m - n) \\ \\
t &= \sqrt{\sqrt{\beta^2 - k} - (\beta + i)/2} - \text{sign}(m-n)\sqrt{|(\beta-i)/2|} \\ \\
F &= t^4 + 2it^2 + 2l(m-n)t + k \\ \\
\frac{dF}{dt} &= 4t^3 + 4it + 2l(m-n) \\ \\
\Delta t &= -F/(dF/dt) \\ \\
u &= t + \Delta t + l \\ \\
v &= t + \Delta t - l \\ \\
\Delta w &= w(1 - 1/u) \\ \\
\Delta z &= {\vec{r}_{\text{z,ECR}}}(1 - (1-\varepsilon^2)/v) \\ \\
\text{Lat} &= \text{arctan2}({\vec{r}_{\text{z,ECR}}}u, wv) \\ \\
\text{Lon} &= \text{arctan2}({\vec{r}_{\text{y,ECR}}}, {\vec{r}_{\text{x,ECR}}}) \\ \\
\text{Alt} &= \text{sign}(u-1)\sqrt{(\Delta w)^2 + (\Delta z)^2}
\end{aligned}}
$$

___

Where:

- ${\vec{r}_{\text{x,ECR}}}, {\vec{r}_{\text{y,ECR}}}, {\vec{r}_{\text{z,ECR}}} :=$ [meters] [ECR position](#D.2.1.1.2 ECI to ECR Position) components from $\vec{r}_{\text{ECR}}$
- $w := $ [meters] horizontal distance from Z-axis
- $l := $ half of first eccentricity squared
- $\varepsilon^2 := $ first eccentricity squared
- $r_a :=$ [meters] Earth semi-major axis (from Earth model)
- $m := $ normalized squared horizontal distance
- $n := $ normalized squared vertical distance
- $p := $ intermediate parameter for quartic equation
- $G := $ product term for feasibility check
- $H := $ feasibility discriminant
- $H_{\min} := \varepsilon^{12}/4 \approx 2.25 \times 10^{-14} $ for WGS84
- $C := $ cube root term for quartic solution
- $i := $ sum parameter
- $\beta := $ quartic solution component
- $k := $ quartic constant term
- $t := $ primary solution parameter of quartic equation
- $F := $ quartic polynomial evaluated at $t $
- $\frac{dF}{dt} := $ derivative of quartic polynomial
- $\Delta t := $ Newton-Raphson correction term
- $u := $ corrected positive offset parameter
- $v := $ corrected negative offset parameter
- $\Delta w := $ [meters] horizontal displacement correction
- $\Delta z := $ [meters] vertical displacement correction
- $\text{sign}(x) := $ sign function returning +1 if $x > 0 $, -1 if $x < 0 $, 0 if $x = 0 $
- $\arctan(y, x) := $ two-argument arctangent function (atan2)
- $\text{Lat} := $ [radians] geodetic latitude
- $\text{Lon} := $ [radians] geodetic longitude
- $\text{Alt} :=$ [meters] geodetic altitude (signed)

___

##### D.2.2.3 ECR to East-North-Up (ENU)

The ECR to ENU transformation establishes a local tangent plane coordinate system at a specified geodetic reference point.

###### D.2.2.3.1 ECR to ENU (DCM)

The reference latitude and longitude define the origin and orientation of the local East-North-Up (ENU) frame. The ECR to ENU transformation consists of two sequential rotations that align the ECR frame with the local tangent plane:

1. A rotation about the Z-axis by $(\pi/2 + \text{Lon}) $ to align the X-axis with the local East direction
2. A rotation about the new X-axis by $(\pi/2 - \text{Lat}) $ to align the Z-axis with the local Up direction

These rotations are expressed using the component rotation matrices:
$$
\mathbf{R}_{\text{yaw}}(\pi/2 + \text{Lon}) = \begin{bmatrix}
-\sin(\text{Lon}) & \cos(\text{Lon}) & 0 \\
-\cos(\text{Lon}) & -\sin(\text{Lon}) & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

$$
\mathbf{R}_{\text{roll}}(\pi/2 - \text{Lat}) = \begin{bmatrix}
1 & 0 & 0 \\
0 & \sin(\text{Lat}) & \cos(\text{Lat}) \\
0 & -\cos(\text{Lat}) & \sin(\text{Lat})
\end{bmatrix}
$$

where the trigonometric identities:
$$
\begin{aligned}
\sin(\pi/2 + \theta) &= \cos(\theta) \\
\cos(\pi/2 + \theta) &= -\sin(\theta) \\
\sin(\pi/2 - \theta) &= \cos(\theta) \\
\cos(\pi/2 - \theta) &= \sin(\theta)
\end{aligned}
$$
have been applied to simplify the expressions.

The composite transformation is:
$$
\mathbf{R}_{\text{ECR to ENU}} = \mathbf{R}_{\text{roll}}(\pi/2 - \text{Lat}) \cdot \mathbf{R}_{\text{yaw}}(\pi/2 + \text{Lon})
$$
Expanding this matrix multiplication yields:
$$
\mathbf{R}_{\text{ECR to ENU}} = \mathbf{R}_{\text{ECR to ENU}}(\text{Lat}, \text{Lon}) = \begin{bmatrix}
-\sin\text{(Lon)} & \cos\text{(Lon)} & 0 \\
-\sin\text{(Lat)}\cos\text{(Lon)} & -\sin\text{(Lat)}\sin\text{(Lon)} & \cos\text{(Lat)} \\
\ \ \ \cos\text{(Lat)}\cos\text{(Lon)} & \ \ \ \cos\text{(Lat)}\sin\text{(Lon)} & \sin\text{(Lat)}
\end{bmatrix}
$$
Where:

- $\mathbf{R}_{\text{ECR to ENU}}(\text{Lat}, \text{Lon}) := $ direction cosine matrix transforming from ECR to ENU frame
- $\mathbf{R}_{\text{roll}} := $ [Roll Rotation Matrix](#D.1.1.1 Roll Rotation Matrix)
- $\mathbf{R}_{\text{yaw}} := $ [Yaw Rotation Matrix](#D.1.1.3 Yaw Rotation Matrix)
- $\text{Lat} := $ [radians] [reference geodetic latitude](#D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA))
- $\text{Lon} :=$ [radians] [reference geodetic longitude](#D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA))

###### D.2.2.3.2 ECR to ENU Position

Position transformation from ECR to ENU requires accounting for Earth's ellipsoidal shape through geoid corrections and prime vertical radius calculations.
$$
\begin{aligned}
{\vec{r}_{\text{ECR}}}' &= \vec{r}_{\text{ECR}} + \begin{bmatrix} 0 \\ 0 \\ z_{geoid} \end{bmatrix} \\ \\
{\vec{r}_{\text{ENU}}}' &= \mathbf{R}_{\text{ECR to ENU}} \cdot {\vec{r}_{\text{ECR}}}' \\ \\ 
\vec{r}_{\text{ENU}} &= {\vec{r}_{\text{ENU}}}' - \begin{bmatrix}0 \\ 0 \\ (r_{pv} + \text{Alt})\end{bmatrix}
\end{aligned}
$$

Where:
- $\vec{r}_{\text{ENU}} :=$ [meters] position vector in ENU frame
- ${\vec{r}_{\text{ECR}}}' :=$ [meters] ECR position with geoid correction applied
- $\vec{r}_{\text{ECR}} :=$ [meters] [position vector in ECR frame](#D.2.1.1.2 ECI to ECR Position)
- $z_{geoid} :=$ [meters] [geoid correction term](#d73-geoid-correction-term)
- ${\vec{r}_{\text{ENU}}}' :=$ [meters] ENU position with altitude correction applied
- $\mathbf{R}_{\text{ECR to ENU}} :=$ [ECR to ENU DCM](#D.2.2.3.1 ECR to ENU (DCM))
- $\text{Alt} :=$ [meters] [reference geodetic altitude](#D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA))
- $r_{pv} :=$ [meters] [prime vertical radius](#d72-prime-vertical-radius)



###### D.2.2.3.3 ECR to ENU Velocity and Acceleration

Velocity and acceleration vectors transform from ECR to ENU frame through rotation only, as both the magnitude and direction of motion must be expressed in the local tangent plane coordinate system.
$$
\begin{aligned}
\vec{v}_{\text{ENU}} &= \mathbf{R}_{\text{ECR to ENU}} \cdot \vec{v}_{\text{ECR}} \\
\vec{a}_{\text{ENU}} &= \mathbf{R}_{\text{ECR to ENU}} \cdot \vec{a}_{\text{ECR}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{ENU}} :=$ [m/s] velocity vector in ENU frame
- $\vec{a}_{\text{ENU}} :=$ [m/s²] acceleration vector in ENU frame
- $\vec{v}_{\text{ECR}} :=$ [m/s] [velocity vector in ECR frame](#D.2.1.1.3 ECI to ECR Velocity)
- $\vec{a}_{\text{ECR}} :=$ [m/s²] [acceleration vector in ECR frame](#D.2.1.1.4 ECI to ECR Acceleration))
- $\mathbf{R}_{\text{ECR to ENU}} :=$ [ECR to ENU DCM](#D.2.2.3.1 ECR to ENU (DCM))

___

#### D.2.3 From ENU

This section defines equations that transform spatial states from ENU frame to other reference frames.

##### D.2.3.1 ENU to ECR

The ENU to ECR transformation is the inverse of the ECR to ENU transformation, requiring altitude and geoid corrections in position transformations.

###### D.2.3.1.1 ENU to ECR (DCM)

The ENU to ECR transformation is the inverse of the ECR to ENU transformation. Since rotation matrices are orthogonal, the inverse equals the transpose.
$$
\mathbf{R}_{\text{ENU to ECR}} = \mathbf{R}_{\text{ENU to ECR}}(\text{Lat}, \text{Lon}) = \mathbf{R}_{\text{ECR to ENU}}^T(\text{Lat}, \text{Lon})
$$

Expanded form:

$$
\mathbf{R}_{\text{ENU to ECR}} = \begin{bmatrix}
-\sin\text{(Lon)} & -\sin\text{(Lat)}\cos\text{(Lon)} & \cos\text{(Lat)}\cos\text{(Lon)} \\
\ \ \ \cos\text{(Lon)} & -\sin\text{(Lat)}\sin\text{(Lon)} & \cos\text{(Lat)}\sin\text{(Lon)} \\
0 & \cos\text{(Lat)} & \sin\text{(Lat)}
\end{bmatrix}
$$

Where:

- $\mathbf{R}_{\text{ENU to ECR}} :=$ direction cosine matrix transforming from ENU to ECR frame
- $\mathbf{R}_{\text{ECR to ENU}}^T :=$ transpose of [ECR to ENU DCM](#D.2.2.3.1 ECR to ENU (DCM))
- $\text{Lat} :=$ [radians] reference geodetic latitude
- $\text{Lon} :=$ [radians] reference geodetic longitude

###### D.2.3.1.2 ENU to ECR Position

$$
\begin{aligned}
{\vec{r}_{\text{ENU}}}' &= \vec{r}_{\text{ENU}} + \begin{bmatrix} 0 \\ 0 \\ (r_{pv} + \text{Alt}) \end{bmatrix} \\ \\
{\vec{r}_{\text{ECR}}}' &= \mathbf{R}_{\text{ENU to ECR}} \cdot {\vec{r}_{\text{ENU}}}' \\ \\
\vec{r}_{\text{ECR}} &= {\vec{r}_{\text{ECR}}}' - \begin{bmatrix} 0 \\ 0 \\ z_{geoid}\end{bmatrix}
\end{aligned}
$$

Where:

- $\vec{r}_{\text{ECR}} :=$ [meters] position vector in ECR frame
- ${\vec{r}_{\text{ENU}}}' :=$ [meters] ENU position with altitude correction applied
- $\vec{r}_{\text{ENU}} :=$ [meters] position vector in ENU frame
- $r_{pv} :=$ [meters] [prime vertical radius](#d72-prime-vertical-radius)
- $\text{Alt} :=$ [meters] reference geodetic altitude
- ${\vec{r}_{\text{ECR}}}' :=$ [meters] ECR position with geoid correction applied

- $\mathbf{R}_{\text{ENU to ECR}} :=$ [ENU to ECR DCM](#D.2.3.1.1 ENU to ECR (DCM))
- $z_{geoid} :=$ [meters] [geoid correction term](#d73-geoid-correction-term)

###### D.2.3.1.3 ENU to ECR Velocity and Acceleration

$$
\begin{aligned}
\vec{v}_{\text{ECR}} &= \mathbf{R}_{\text{ENU to ECR}} \cdot \vec{v}_{\text{ENU}} \\
\vec{a}_{\text{ECR}} &= \mathbf{R}_{\text{ENU to ECR}} \cdot \vec{a}_{\text{ENU}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{ECR}} :=$ [m/s] velocity vector in ECR frame
- $\vec{a}_{\text{ECR}} :=$ [m/s²] acceleration vector in ECR frame
- $\vec{v}_{\text{ENU}} :=$ [m/s] velocity vector in ENU frame
- $\vec{a}_{\text{ENU}} :=$ [m/s²] acceleration vector in ENU frame
- $\mathbf{R}_{\text{ENU to ECR}} :=$ [ENU to ECR DCM](#D.2.3.1.1 ENU to ECR (DCM))

##### D.2.3.2 ENU to North-East-Down (NED)

The ENU to NED transformation is a simple axis permutation and sign change, requiring no additional parameters beyond the coordinate swap.

###### D.2.3.2.1 ENU to NED (DCM)

$$
\mathbf{R}_{\text{ENU to NED}} = \begin{bmatrix} 
0 & 1 & 0 \\ 
1 & 0 & 0 \\ 
0 & 0 & -1 
\end{bmatrix}
$$

Where:

- $\mathbf{R}_{\text{ENU to NED}} :=$ direction cosine matrix transforming from ENU to NED frame

###### D.2.3.2.2 ENU to NED Position, Velocity, and Acceleration

$$
\begin{aligned}
\text{North}_{\text{NED}} &= \text{North}_{\text{ENU}} \\
\text{East}_{\text{NED}} &= \text{East}_{\text{ENU}} \\
\text{Down}_{\text{NED}} &= -\text{Up}_{\text{ENU}}
\end{aligned}
$$

In matrix form:

$$
\begin{bmatrix} \text{North} \\ \text{East} \\ \text{Down} \end{bmatrix} = \mathbf{R}_{\text{ENU to NED}} \cdot \begin{bmatrix} \text{East} \\ \text{North} \\ \text{Up} \end{bmatrix}
$$

This transformation applies identically to position, velocity, and acceleration vectors:

$$
\begin{aligned}
\vec{r}_{\text{NED}} &= \mathbf{R}_{\text{ENU to NED}} \cdot \vec{r}_{\text{ENU}} \\
\vec{v}_{\text{NED}} &= \mathbf{R}_{\text{ENU to NED}} \cdot \vec{v}_{\text{ENU}} \\
\vec{a}_{\text{NED}} &= \mathbf{R}_{\text{ENU to NED}} \cdot \vec{a}_{\text{ENU}}
\end{aligned}
$$

Where:

- $\vec{r}_{\text{NED}} :=$ [meters] position vector in NED frame
- $\vec{v}_{\text{NED}} :=$ [m/s] velocity vector in NED frame
- $\vec{a}_{\text{NED}} :=$ [m/s²] acceleration vector in NED frame
- $\vec{r}_{\text{ENU}} :=$ [meters] position vector in ENU frame
- $\vec{v}_{\text{ENU}} :=$ [m/s] velocity vector in ENU frame
- $\vec{a}_{\text{ENU}} :=$ [m/s²] acceleration vector in ENU frame
- $\mathbf{R}_{\text{ENU to NED}} :=$ [ENU to NED DCM](#D.2.3.2.1 ENU to NED (DCM))

___

#### D.2.4 From NED

This section defines equations that transform spatial states from NED frame to other reference frames.

##### D.2.4.1 NED to East-North-Up (ENU)

The NED to ENU transformation is the inverse of the ENU to NED transformation, consisting of the same axis permutation and sign change.

###### D.2.4.1.1 NED to ENU (DCM)

The NED to ENU transformation is the inverse of the ENU to NED transformation. Since the rotation matrix is orthogonal and symmetric in this case, the inverse equals the transpose, which equals the original matrix.
$$
\mathbf{R}_{\text{NED to ENU}} = \mathbf{R}_{\text{ENU to NED}}^T = \begin{bmatrix} 
0 & 1 & 0 \\ 
1 & 0 & 0 \\ 
0 & 0 & -1 
\end{bmatrix}
$$

Where:

- $\mathbf{R}_{\text{NED to ENU}} :=$ direction cosine matrix transforming from NED to ENU frame
- $\mathbf{R}_{\text{ENU to NED}}^T :=$ transpose of [ENU to NED DCM](#D.2.3.2.1 ENU to NED (DCM))

###### D.2.4.1.2 NED to ENU Position, Velocity, and Acceleration

$$
\begin{aligned}
\text{East}_{\text{ENU}} &= \text{East}_{\text{NED}} \\
\text{North}_{\text{ENU}} &= \text{North}_{\text{NED}} \\
\text{Up}_{\text{ENU}} &= -\text{Down}_{\text{NED}}
\end{aligned}
$$

In matrix form:

$$
\begin{bmatrix} \text{East} \\ \text{North} \\ \text{Up} \end{bmatrix} = \mathbf{R}_{\text{NED to ENU}} \cdot \begin{bmatrix} \text{North} \\ \text{East} \\ \text{Down} \end{bmatrix}
$$

This transformation applies identically to position, velocity, and acceleration vectors:

$$
\begin{aligned}
\vec{r}_{\text{ENU}} &= \mathbf{R}_{\text{NED to ENU}} \cdot \vec{r}_{\text{NED}} \\
\vec{v}_{\text{ENU}} &= \mathbf{R}_{\text{NED to ENU}} \cdot \vec{v}_{\text{NED}} \\
\vec{a}_{\text{ENU}} &= \mathbf{R}_{\text{NED to ENU}} \cdot \vec{a}_{\text{NED}}
\end{aligned}
$$

Where:

- $\vec{r}_{\text{ENU}} :=$ [meters] position vector in ENU frame
- $\vec{v}_{\text{ENU}} :=$ [m/s] velocity vector in ENU frame
- $\vec{a}_{\text{ENU}} :=$ [m/s²] acceleration vector in ENU frame
- $\vec{r}_{\text{NED}} :=$ [meters] position vector in NED frame
- $\vec{v}_{\text{NED}} :=$ [m/s] velocity vector in NED frame
- $\vec{a}_{\text{NED}} :=$ [m/s²] acceleration vector in NED frame
- $\mathbf{R}_{\text{NED to ENU}} :=$ [NED to ENU DCM](#D.2.4.1.1 NED to ENU (DCM))

___

#### D.2.5 From LLA

This section contains definitions of all equations that transform from Latitude-Longitude-Altitude (LLA) frame to another frame

##### D.2.5.1 LLA to ECR

The LLA to ECR transformation converts geodetic position coordinates (latitude, longitude, altitude) to Cartesian coordinates in the ECR frame, accounting for Earth's ellipsoidal shape through the prime vertical radius.

###### D.2.5.1.1 LLA to ECR Position

$$
\begin{aligned}
X &= (r_{\text{pv}} + \text{Alt}) \cos(\text{Lat}) \cos(\text{Lon}) \\ \\
Y &= (r_{\text{pv}} + \text{Alt}) \cos(\text{Lat}) \sin(\text{Lon}) \\ \\
Z &= (r_{\text{pv}}(1 - \varepsilon^2) + \text{Alt}) \sin(\text{Lat}) \\ \\
\vec{r}_{\text{ECR}} &= \begin{bmatrix} X \\ Y \\ Z \end{bmatrix}
\end{aligned}
$$

Where:

- $X, Y, Z := $ [meters] ECR position components
- $\vec{r}_{\text{ECR}} := $ [meters] position vector in ECR frame
- $r_{\text{pv}} := $ [meters] [prime vertical radius](#d72-prime-vertical-radius) at reference latitude
- $\varepsilon^2 := $ first eccentricity squared (from Earth model)
- $\text{Lat} := $ [radians] geodetic latitude
- $\text{Lon} := $ [radians] geodetic longitude
- $\text{Alt} :=$ [meters] geodetic altitude

___

#### D.2.6 From Body CG

This section contains definitions of all equations that transform from Body Center of Gravity (Body CG) frame to another frame.

##### D.2.6.1 Body CG to ECI

The Body CG to ECI transformation is the inverse of the ECI to Body CG transformation, rotating vectors from the body-fixed frame centered at the missile's center of gravity to the inertial reference frame.

###### D.2.6.1.1 Body CG to ECI (DCM)

The direction cosine matrix transforming from Body CG to ECI frame is the transpose of the ECI to Body CG DCM, constructed from Euler angles obtained through [quaternion conversion](#D.1.2.1 Quaternion to Euler Angles).
$$
\mathbf{R}_{\text{BodyCG to ECI}} = \mathbf{R}_{\text{BodyCG to ECI}}(\phi_{B2I}, \theta_{B2I}, \psi_{B2I}) = \mathbf{R}_{\text{ECI to BodyCG}}^T(\phi_{I2B}, \theta_{I2B}, \psi_{I2B})
$$

Where:

- $\mathbf{R}_{\text{BodyCG to ECI}} :=$ direction cosine matrix transforming from Body CG to ECI frame
- $\mathbf{R}_{\text{ECI to BodyCG}}^T :=$ transpose of [ECI to Body CG DCM](#D.2.1.2.1 ECI to Body CG (DCM))

###### D.2.6.1.2 Body CG to ECI Position

Since the Body CG frame origin is located at the missile's center of gravity, its position in the Body CG frame is always $[0, 0, 0]$. The missile's ECI position is stored directly in the trajectory data:  [`x_pos_eci`, `y_pos_eci`, `z_pos_eci`].

###### D.2.6.1.3 Body CG to ECI Velocity and Acceleration

Velocity and acceleration vectors transform from Body CG to ECI frame through rotation only, as both velocity and acceleration are defined at the center of gravity.
$$
\begin{aligned}
\vec{v}_{\text{ECI}} &= \mathbf{R}_{\text{BodyCG to ECI}} \cdot \vec{v}_{\text{BodyCG}} \\
\vec{a}_{\text{ECI}} &= \mathbf{R}_{\text{BodyCG to ECI}} \cdot \vec{a}_{\text{BodyCG}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{ECI}} :=$ [m/s] velocity vector in ECI frame
- $\vec{a}_{\text{ECI}} :=$ [m/s²] acceleration vector in ECI frame
- $\vec{v}_{\text{BodyCG}} :=$ [m/s] velocity vector in Body CG frame
- $\vec{a}_{\text{BodyCG}} :=$ [m/s²] acceleration vector in Body CG frame
- $\mathbf{R}_{\text{BodyCG to ECI}} :=$ [Body CG to ECI DCM](#D.2.6.1.1 Body CG to ECI (DCM))

##### D.2.6.2 Body CG to Body Nose

The Body CG to Body Nose transformation translates between two body-fixed coordinate frames that share the same orientation but have different origin locations along the missile's longitudinal axis.

###### D.2.6.2.1 Body CG to Body Nose Position

Position transformation from Body CG to Body Nose frame requires adding the center of gravity offset vector, as the frames differ only in origin location along the body X-axis.
$$
\begin{align}
\vec{r}_{\text{BodyNose}} &= \vec{r}_{\text{BodyCG}} + \vec{r}_{\text{CG}}
\end{align}
$$

Where:

- $\vec{r}_{\text{BodyNose}} :=$ [meters] position vector in Body Nose frame
- $\vec{r}_{\text{BodyCG}} :=$ [meters] position vector in Body CG frame
- $\vec{r}_{\text{CG}} :=$ [meters] the CG of the missile in Body Nose frame: [`x_pos_center_gravity`,  `y_pos_center_gravity`, `z_pos_center_gravity`]

###### D.2.6.2.2 Body CG to Body Nose Velocity and Acceleration

Since the Body CG and Body Nose frames share the same orientation and move together rigidly, velocity and acceleration vectors are identical in both frames:

$$
\begin{aligned}
\vec{v}_{\text{BodyNose}} &= \vec{v}_{\text{BodyCG}} \\
\vec{a}_{\text{BodyNose}} &= \vec{a}_{\text{BodyCG}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{BodyNose}} :=$ [m/s] velocity vector in Body Nose frame
- $\vec{v}_{\text{BodyCG}} :=$ [m/s] velocity vector in Body CG frame
- $\vec{a}_{\text{BodyNose}} :=$ [m/s²] acceleration vector in Body Nose frame
- $\vec{a}_{\text{BodyCG}} :=$ [m/s²] acceleration vector in Body CG frame

___

#### D.2.7 From Body Nose

This section contains definitions of all equations that transform from Body Nose frame to another frame.

##### D.2.7.1 Body Nose to Body CG

The Body Nose to Body CG transformation is the inverse of the Body CG to Body Nose transformation, translating from the nose reference point back to the center of gravity reference point.

###### D.2.7.1.1 Body Nose to Body CG Position

Position transformation from Body Nose to Body CG frame requires subtracting the center of gravity offset vector, as the frames differ only in origin location along the body X-axis.
$$
\begin{align}
\vec{r}_{\text{BodyCG}} &= \vec{r}_{\text{BodyNose}} - \vec{r}_{\text{CG}}
\end{align}
$$

Where:

- $\vec{r}_{\text{BodyCG}} :=$ [meters] position vector in Body CG frame
- $\vec{r}_{\text{BodyNose}} :=$ [meters] position vector in Body Nose frame
- $\vec{r}_{\text{CG}} :=$ [meters] the CG of the missile in Body Nose frame: [`x_pos_center_gravity`, `y_pos_center_gravity`, `z_pos_center_gravity`]

###### D.2.7.1.2 Body Nose to Body CG Velocity and Acceleration

Since the Body Nose and Body CG frames share the same orientation and move together rigidly, velocity and acceleration vectors are identical in both frames:

$$
\begin{aligned}
\vec{v}_{\text{BodyCG}} &= \vec{v}_{\text{BodyNose}} \\
\vec{a}_{\text{BodyCG}} &= \vec{a}_{\text{BodyNose}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{BodyCG}} :=$ [m/s] velocity vector in Body CG frame
- $\vec{v}_{\text{BodyNose}} :=$ [m/s] velocity vector in Body Nose frame
- $\vec{a}_{\text{BodyCG}} :=$ [m/s²] acceleration vector in Body CG frame
- $\vec{a}_{\text{BodyNose}} :=$ [m/s²] acceleration vector in Body Nose frame

___

### D.3 Flight Data

This section contains a collection of equations defining various aspects of flight data to be used in aerodynamics calculations.

#### D.3.1 Airspeed

##### D.3.1.1 ECI Airspeed

ECI airspeed represents the velocity of the object relative to the surrounding air mass, with vector components expressed in the inertial ECI frame. This quantity accounts for both the object's motion relative to Earth's surface and the motion of the air mass itself.
$$
\begin{aligned}
\vec{v}_{\text{air,ECI}} &= \vec{v}_{\text{relative,ECI}} - \vec{v}_{\text{wind, ECI}}
\end{aligned}
$$

Where:

- $\vec{v}_{\text{air,ECI}} :=$ [m/s] airspeed vector in ECI frame
- $\vec{v}_{\text{relative,ECI}} :=$ [m/s] [relative velocity vector in ECI frame](#D.2.0.4 Relative Velocity (ECI))
- $\vec{v}_{\text{wind,ECI}} :=$ [m/s] wind velocity vector in ECI frame: [`x_vel_eci_wind`, `y_vel_eci_wind`, `z_vel_eci_wind`]

##### D.3.1.2 Body CG Airspeed

Body CG airspeed represents the airspeed vector rotated into the body-fixed reference frame with origin at the center of gravity. This transformation enables aerodynamic force and moment calculations that depend on airflow direction relative to the body axes.

The Body CG airspeed is obtained by rotating the [airspeed vector in ECI frame](#D.3.1.1 ECI Airspeed) using this composite DCM:
$$
\vec{v}_{\text{air,BodyCG}} = \mathbf{R}_{\text{ECI to BodyCG}} \cdot \vec{v}_{\text{air,ECI}}
$$

Where:

- $\vec{v}_{\text{air,BodyCG}} :=$ [m/s] airspeed vector in Body CG frame
- $\mathbf{R}_{\text{ECI to BodyCG}} :=$ [ECI to Body CG DCM](#D.2.1.2.1 ECI to Body CG (DCM))
- $\vec{v}_{\text{air,ECI}} :=$ [m/s] [airspeed vector in ECI frame](#D.3.1.1 ECI Airspeed)

#### D.3.2 Angle of Attack

Angle of attack quantifies the orientation of the object's body axis relative to the airspeed vector. These angles determine the aerodynamic forces and moments acting on the object.

##### D.3.2.1 Total Angle of Attack

The total angle of attack represents the angle between the body's longitudinal axis (x-axis) and the airspeed vector, regardless of the plane of rotation.
$$
\large{\text{aoa}_{\text{total}} = \begin{cases} 
0 & \text{if } \|\vec{v}_{\text{air,BodyCG}}\| = 0 \\[6pt]
\arccos\left(\frac{v_{x\text{,(air,BodyCG)}}}{\|\vec{v}_{\text{air,BodyCG}}\|}\right) & \text{otherwise}
\end{cases}}
$$
Where:

- $\text{aoa}_{\text{total}} :=$ [radians] total angle of attack
- $v_{x\text{,(air,BodyCG)}} := $ [m/s] x-component of [airspeed in Body CG frame](#D.3.1.2 Body CG Airspeed)
- $\vec{v}_{\text{air,BodyCG}} :=$ [m/s] [airspeed vector in Body CG frame](#D.3.1.2 Body CG Airspeed)

##### D.3.2.2 Pitch Angle of Attack

The pitch angle of attack is the angle between the body x-axis and the projection of the airspeed vector onto the body x-z plane.

$$
\text{aoa}_\alpha = \text{arctan2}(v_{z\text{,(air,BodyCG)}}, v_{x\text{,(air,BodyCG)}})
$$

Where:

- $\text{aoa}_\alpha :=$ [radians] pitch angle of attack (alpha)
- $v_{z\text{,(air,BodyCG)}} :=$ [m/s] z-component of [airspeed in Body CG frame](#D.3.1.2 Body CG Airspeed)
- $v_{x\text{,(air,BodyCG)}} :=$ [m/s] x-component of [airspeed in Body CG frame](#D.3.1.2 Body CG Airspeed)

##### D.3.2.3 Yaw Angle of Attack

The yaw angle of attack (side slip angle) is the angle between the body x-axis and the projection of the airspeed vector onto the body x-y plane.

$$
\text{aoa}_\beta = \text{arctan2}(v_{y\text{,(air,BodyCG)}}, v_{x\text{,(air,BodyCG)}})
$$

Where:

- $\text{aoa}_\beta :=$ [radians] yaw angle of attack (beta)
- $v_{y\text{,(air,BodyCG)}} :=$ [m/s] y-component of [airspeed in Body CG frame](#D.3.1.2 Body CG Airspeed)
- $v_{x\text{,(air,BodyCG)}} :=$ [m/s] x-component of [airspeed in Body CG frame](#D.3.1.2 Body CG Airspeed)

#### D.3.3 Flight Path Angle

The flight path angle represents the angle between the velocity vector and the local horizontal plane. This angle characterizes the climb or descent trajectory of the object.

##### D.3.3.1 Flight Path Angle in ECR Frame

The flight path angle in the ECR frame represents the angle relative to Earth's surface, as observed by ground-based observers.

The local vertical unit vector is calculated from geodetic coordinates:

$$
\hat{r}_{\text{local}} = \begin{bmatrix}
\cos(\text{Lat}) \cos(\text{Lon}) \\
\cos(\text{Lat}) \sin(\text{Lon}) \\
\sin(\text{Lat})
\end{bmatrix}
$$

$$
\text{fpa}_{\text{ECR}} = \arcsin\left(\frac{\vec{v}_{\text{ECR}} \cdot \hat{r}_{\text{local}}}{\|\vec{v}_{\text{ECR}}\|}\right)
$$

Where:

- $\text{fpa}_{\text{ECR}} :=$ [radians] flight path angle in ECR frame (positive = climbing)
- $\vec{v}_{\text{ECR}} :=$ [m/s] [velocity vector in ECR frame](#D.2.1.1.3 ECI to ECR Velocity)
- $\hat{r}_{\text{local}} :=$ local vertical unit vector (from Earth center through position)
- $\text{Lat} :=$ [radians] geodetic latitude from [ECR to LLA](#D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA))
- $\text{Lon} :=$ [radians] geodetic longitude from [ECR to LLA](#D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA))

##### D.3.3.2 Inertial Flight Path Angle

The inertial flight path angle represents the flight path angle calculated in the inertial reference frame using ECI velocity. Although the geodetic coordinate transformation algorithms are designed for the rotating ECR frame, certain legacy trajectory formats require the inertial flight path angle, necessitating the application of the [ECR to LLA coordinate transformation algorithm](#D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA)) to ECI position vectors. This approach, while mixing reference frames unconventionally, produces the values required for compatibility with established trajectory data specifications.

To calculate the inertial flight path angle, apply the ECR to LLA coordinate transformation algorithm to the ECI position vector to determine the local vertical direction:
$$
\begin{align}
(\text{Lat}_{\text{ECI}}, \text{Lon}_{\text{ECI}}, \text{Alt}_{\text{ECI}})  = \text{ECR\_to\_LLA}(\vec{r}_{ECI}) \\ \\
\hat{r}_{\text{local, ECI}} = \begin{bmatrix}
\cos(\text{Lat}_{\text{ECI}}) \cdot \cos(\text{Lon}_{\text{ECI}}) \\
\cos(\text{Lat}_{\text{ECI}}) \cdot \sin(\text{Lon}_{\text{ECI}}) \\
\sin(\text{Lat}_{\text{ECI}})
\end{bmatrix}
\end{align}
$$


Then the ECI velocity vector is projected onto this direction:
$$
\text{fpa}_{\text{ECI}} = \arcsin\left(\frac{\vec{v}_{\text{ECI}} \cdot \hat{r}_{\text{local, ECI}}}{\|\vec{v}_{\text{ECI}}\|}\right)
$$

Where:

- $\text{fpa}_{\text{ECI}} :=$ [radians] inertial flight path angle
- $\vec{r}_{\text{ECI}} := $ [meters] position vector in ECI frame: [ `x_pos_eci`, `y_pos_eci`, `z_pos_eci`]
- $(\text{Lat}_{\text{ECI}}, \text{Lon}_{\text{ECI}}, \text{Alt}_{\text{ECI}}) := $ [radians, radians, meters] geodetic coordinates derived from ECI position using [ECR to LLA algorithm](#D.2.2.2 ECR to Latitude-Longitude-Altitude (LLA))
- $\hat{r}_{\text{local, ECI}} := $ local vertical unit vector calculated from ECI position
- $\vec{v}_{\text{ECI}} := $ [m/s] velocity vector in ECI frame: [ `x_vel_eci`, `y_vel_eci`, `z_vel_eci`]

#### D.3.4 Precession and Spin

Precession and spin describe the rotational motion of an object about its center of mass. These parameters characterize the stability and tumbling behavior during flight.

##### D.3.4.1 Lateral Angular Rate Magnitude

The lateral angular rate magnitude represents the combined magnitude of pitch and yaw angular rates. This quantity characterizes the object's rotational motion perpendicular to its longitudinal axis.

$$
\omega_s = \sqrt{\omega_{q,Body}^2 + \omega_{r,Body}^2}
$$


Where:

- $\omega_s :=$ [rad/s] lateral angular rate magnitude
- $\omega_{q, Body} :=$ [rad/s] pitch rate of the body in Body CG frame: `pit_rate`
- $\omega_{r, Body}:=$ [rad/s] yaw rate of the body in Body CG frame: `yaw_rate`

##### D.3.4.2 Precession Angle

The precession angle represents the angle between the angular momentum vector and the body longitudinal axis (x-axis). This angle characterizes the coning motion of the object. Valid values range from 0 to 90 degrees (0 to π/2 radians).

$$
\large{\begin{aligned}
\vec{H}_{BodyCG} &= \mathbf{I}_{\text{BodyCG}} \cdot \omega_{Body} \\ \\
\text{precession} &= \begin{cases} 
\frac{\pi}{2} & \text{if } \omega_{p,Body} = 0 \\ 
 \arccos\left(\frac{\vec{H}_{BodyCG} \cdot \omega_{p,Body}}{\|\vec{H}_{BodyCG} \|}\right) & \text{otherwise} 
\end{cases}
\end{aligned}}
$$

Where:

- $\text{precession} :=$ [radians] precession angle (coning half angle), range [0, π/2]
- $I_{BodyCG} :=$ [kg·m²] [inertia tensor](#D.5.1 Inertia Tensor Definition)
- $\omega_{p,Body} :=$ [rad/s] roll rate of the body in Body CG frame: `rol_rate` 
- $\omega_{Body} :=$ [rad/s] body rates in Body CG frame: `[rol_rate, pit_rate, yaw_rate]`
- $\vec{H}_{BodyCG} :=$ ???
##### D.3.4.3 Precession Rate

The precession rate represents the rate at which the body axis precesses about the angular momentum vector. This rate characterizes the frequency of the coning motion.

$$
\dot{\text{precession}} = \begin{cases}
0 & \text{if } \text{precession} \approx 0 \\
\frac{\omega_s}{\sin(precession)} & \text{otherwise}
\end{cases}
$$

Where:

- $\dot{\text{precession}} :=$ [rad/s] precession rate (coning rate)
- $\omega_s :=$ [rad/s] [lateral angular rate magnitude](#d341-lateral-angular-rate-magnitude)
- $\text{precession} :=$ [radians] [precession angle](#d342-precession-angle)

##### D.3.4.4 Spin Angle

The spin angle represents the cumulative angular rotation about the longitudinal body axis (x-axis) since trajectory initialization. This value tracks how much the object has spun in total, wrapped to maintain values within the range [-180°, 180°] (-π to +π radians).

> The spin angle differs from the Euler roll angle φ: the Euler roll angle represents the instantaneous orientation of the body frame relative to a reference frame, while the spin angle accumulates the total rotation about the body's longitudinal axis over time. A rapidly spinning projectile will repeatedly wrap through ±π as it completes full rotations.

$$
\phi_{\text{spin}}(t) = \phi_{\text{spin}}(t_{0, \text{obj}}) + \int_{t_{0, \text{obj}}}^{t} \omega_{p,Body}(\tau) \, d\tau
$$

The accumulated value is then wrapped to the range [-π, π] by repeating the below assignment until $-\pi \leq \phi_{\text{spin}} \leq \pi$ :
$$
\phi_{\text{spin}} = \begin{cases} \phi_{\text{spin}} - 2\pi & \text{if } \phi_{\text{spin}} \gt +\pi \\\phi_{\text{spin}} + 2\pi & \text{if } \phi_{\text{spin}} \lt -\pi\\\phi_{\text{spin}} & \text{otherwise} \end{cases}
$$

Where:

- $\phi_{\text{spin}}(t) :=$ [radians] spin angle at time t, range [-π, π]
- $\phi_{\text{spin}}(t_{0, \text{obj}}) :=$ [radians] initial spin angle of this object at $t_{0, \text{obj}}$
- $t_{0, \text{obj}} :=$ [seconds] initial time of this object's trajectory: `Trajectory[0].time`
- $t :=$ [seconds] current trajectory time: `Trajectory[i].time`
- $\omega_{p,Body}(\tau) :=$ [rad/s] roll rate of the body in Body CG frame as a function of time: `rol_rate`


##### D.3.4.5 Spin Rate

The spin rate represents the rate of change of the spin angle about the longitudinal body axis. Spin rate can also be considered the roll rate in a body frame.

$$
\dot{\phi}_{\text{spin}} = \dot{\phi}
$$

Where:

- $\dot{\phi}_{\text{spin}} :=$ [rad/s] spin rate
- $\omega_{p,Body} :=$ [rad/s] roll rate of the body in Body CG frame: `rol_rate`

#### D.3.5 Mach Number

The Mach number represents the ratio of airspeed to the local speed of sound, characterizing the compressibility regime of the flow.

$$
v_{\text{sound}} = \sqrt{\gamma_{\text{air}} \cdot R_{\text{air}} \cdot T_{\text{atmos}}}
$$

$$
\text{mach} = \frac{\|\vec{v}_{\text{air,ECI}}\|}{v_{\text{sound}}}
$$

Where:

- $\text{mach} :=$ Mach number (dimensionless)
- $\vec{v}_{\text{air,ECI}} :=$ [m/s] [airspeed vector in ECI frame](#d31-airspeed)
- $v_{\text{sound}} :=$ [m/s] speed of sound in air
- $\gamma_{\text{air}} :=$ 1.4 (specific heat ratio for air, dimensionless)
- $R_{\text{air}} :=$ 287.052874247 J/(kg·K) (specific gas constant for air @ standard sea level conditions)
- $T_{\text{atmos}} :=$ [K] atmospheric temperature: `temperature_atmospheric`

#### D.3.6 Sensed Acceleration

The sensed acceleration represents the acceleration measured by an onboard accelerometer or inertial measurement unit (IMU). Physical accelerometers measure the non-gravitational acceleration experienced by the object. The sensed acceleration is exclusively expressed in the Body CG frame to align with the physical orientation of onboard sensors. An object in free fall would experience no sensed acceleration.

##### D.3.6.1 ECI Sensed Acceleration

The sensed acceleration calculation begins in the ECI frame by removing gravitational acceleration from the total acceleration:

$$
\vec{a}_{\text{sensed,ECI}} = \vec{a}_{\text{ECI}} - \vec{a}_{\text{gravity,ECI}}
$$

Where:

- $\vec{a}_{\text{sensed,ECI}} :=$ [m/s²] sensed acceleration vector in ECI frame
- $\vec{a}_{\text{ECI}} :=$ [m/s²] acceleration vector in ECI frame: [`x_acc_eci`, `y_acc_eci`, `z_acc_eci`]
- $\vec{a}_{\text{gravity,ECI}} :=$ [m/s²] gravitational acceleration vector in ECI frame: [`x_acc_eci_gravity`, `y_acc_eci_gravity`, `z_acc_eci_gravity`]

##### D.3.6.2 Body CG Sensed Acceleration

The sensed acceleration vector is then transformed from the ECI frame to the Body CG frame using the rotation matrix:

$$
\vec{a}_{\text{sensed,BodyCG}} = \mathbf{R}_{\text{ECI to BodyCG}} \cdot \vec{a}_{\text{sensed,ECI}}
$$

Where:

- $\vec{a}_{\text{sensed,BodyCG}} :=$ [m/s²] sensed acceleration vector in Body CG frame: $[a*{x,\text{sensed}}, a_{y,\text{sensed}}, a_{z,\text{sensed}}]$
- $\mathbf{R}_{\text{ECI to BodyCG}} :=$ [ECI to Body CG DCM](#D.2.1.2.1 ECI to Body CG (DCM))
- $\vec{a}_{\text{sensed,ECI}} :=$ [m/s²] [sensed acceleration vector in ECI frame](#d361-eci-sensed-acceleration)

> The x-component of the Body CG sensed acceleration ($a_{x,\text{sensed}}$) is traditionally referred to as the sensed axial acceleration.

##### D.3.6.3 Lateral Sensed Acceleration

The lateral sensed acceleration represents the magnitude of sensed acceleration perpendicular to the body longitudinal axis. This quantity characterizes the transverse acceleration experienced by the object.

$$
a_{\text{lateral,sensed}} = \sqrt{a_{y,\text{sensed}}^2 + a_{z,\text{sensed}}^2}
$$

Where:

- $a_{\text{lateral,sensed}} :=$ [m/s²] lateral sensed acceleration magnitude
- $a_{y,\text{sensed}} :=$ [m/s²] y-component of [sensed acceleration in Body CG frame](#d362-body-cg-sensed-acceleration)
- $a_{z,\text{sensed}} :=$ [m/s²] z-component of [sensed acceleration in Body CG frame](#d362-body-cg-sensed-acceleration)


___

### D.4 Aerodynamic Coefficients

This section defines aerodynamic force coefficients and the quantities required for their calculation. These dimensionless coefficients normalize aerodynamic forces by dynamic pressure and reference area, enabling comparison across different flight conditions and vehicle geometries.

#### D.4.1 Dynamic Pressure

Dynamic pressure represents the kinetic energy per unit volume of the airflow around the object. This quantity scales aerodynamic forces and moments acting on the object.

$$
P_{\text{dynamic}} = \frac{1}{2} \rho_{\text{atmos}} \cdot \|\vec{v}_{\text{air,BodyCG}}\|^2
$$

Where:

- $P_{\text{dynamic}} :=$ [Pa] dynamic pressure
- $\rho_{\text{atmos}} :=$ [kg/m³] atmospheric density: `density_atmospheric`
- $\vec{v}_{\text{air,BodyCG}} :=$ [m/s] [airspeed vector in body frame](#d31-airspeed)

#### D.4.2 Reference Area

The reference area is a characteristic area used to non-dimensionalize aerodynamic forces. This value is derived from the ballistic coefficient relationship when both ballistic coefficient and drag coefficient are known.

$$
S_{\text{ref}} = \frac{m}{C_{Ballistic} \cdot C_D}
$$

Where:

- $S_{\text{ref}} :=$ [m²] aerodynamic reference area
- $m :=$ [kg] object mass: `mass`
- $C_{Ballistic} :=$ [kg/m²] ballistic coefficient: `coefficient_ballistic`
- $C_D :=$ drag coefficient: `coefficient_drag`

#### D.4.3 Axial Force Coefficient

The axial force coefficient represents the component of aerodynamic force along the body longitudinal axis (x-axis), normalized by dynamic pressure and reference area.

$$
C_a = \frac{F_{x,\text{aero}}}{P_{\text{dynamic}} \cdot S_{\text{ref}}}
$$

Where:

- $C_a :=$ axial force coefficient
- $F_{x,\text{aero}} :=$ [N] aerodynamic force along body x-axis: `x_force_aero`
- $P_{\text{dynamic}} :=$ [Pa] [dynamic pressure](#D.4.1 Dynamic Pressure)
- $S_{\text{ref}} :=$ [m²] [reference area](#D.4.2 Reference Area)

#### D.4.4 Normal Force Coefficient

The normal force coefficient represents the component of aerodynamic force along the body ventral axis (z-axis), normalized by dynamic pressure and reference area.

$$
C_n = \frac{F_{z,\text{aero}}}{P_{\text{dynamic}} \cdot S_{\text{ref}}}
$$

Where:

- $C_n :=$ normal force coefficient
- $F_{z,\text{aero}} :=$ [N] aerodynamic force along body z-axis: `z_force_aero`
- $P_{\text{dynamic}} :=$ [Pa] [dynamic pressure](#D.4.1 Dynamic Pressure)
- $S_{\text{ref}} :=$ [m²] [reference area](#D.4.2 Reference Area)

#### D.4.5 Lift Coefficient

The lift coefficient represents the aerodynamic force component perpendicular to the airspeed direction, normalized by dynamic pressure and reference area. This coefficient is derived by transforming body-axis force coefficients into the wind-axis reference frame using the pitch angle of attack.

$$
C_L = -\sin(\text{aoa}_\alpha) \cdot C_a + \cos(\text{aoa}_\alpha) \cdot C_n
$$

Where:

- $C_L :=$ lift coefficient (dimensionless)
- $\text{aoa}_\alpha :=$ [radians] [pitch angle of attack](#D.3.2.2 Pitch Angle of Attack)
- $C_a :=$ [axial force coefficient](#D.4.3 Axial Force Coefficient)
- $C_n :=$ [normal force coefficient](#D.4.4 Normal Force Coefficient)

___

### D.5 Mass Properties

#### D.5.1 Inertia Tensor Definition

The inertia tensor is a symmetric 3×3 matrix that characterizes the mass distribution of the object relative to the Body CG coordinate frame. The tensor quantifies the object's resistance to rotational acceleration about each axis and describes coupling between rotational axes.

##### D.5.1.1 Inertia Tensor Matrix Form

The inertia tensor in the Body CG frame takes the form: 
$$
\mathbf{I}_{\text{BodyCG}} = \begin{bmatrix} 
I_{xx} & I_{xy} & I_{xz} \\
I_{yx} & I_{yy} & I_{yz} \\
I_{zx} & I_{zy} & I_{zz} 
\end{bmatrix}
$$
Where:

- $\mathbf{I}_{\text{BodyCG}} :=$ [kg·m²] inertia tensor matrix in Body CG frame
- $I_{xx}, I_{yy}, I_{zz} :=$ [kg·m²] moments of inertia about the x, y, and z axes
- $I_{xy}, I_{xz}, I_{yz} :=$ [kg·m²] products of inertia

##### D.5.1.2 Moments of Inertia

The moments of inertia represent the object's resistance to rotation about each principal body axis. Each moment is the mass-weighted integral of the squared perpendicular distance from the rotation axis.

$$
\begin{aligned} 
I_{xx} &= \int_V \rho_\text{mass}(y^2 + z^2) \ dV \\
I_{yy} &= \int_V \rho_\text{mass}(x^2 + z^2) \ dV \\
I_{zz} &= \int_V \rho_\text{mass}(x^2 + y^2) \ dV 
\end{aligned}
$$

Where:

- $I_{xx} :=$ [kg·m²] moment of inertia about the x-axis: `xx_moment_inertia`
- $I_{yy} :=$ [kg·m²] moment of inertia about the y-axis: `yy_moment_inertia`
- $I_{zz} :=$ [kg·m²] moment of inertia about the z-axis: `zz_moment_inertia`
- $\rho_\text{mass} :=$ [kg/m³] mass density at position (x, y, z) in Body CG frame
- $x, y, z :=$ [meters] coordinates in Body CG frame
- $V :=$ [meters³] volume of the object

##### D.5.1.3 Products of Inertia

The products of inertia quantify the coupling between rotational motion about different axes. Non-zero products of inertia indicate mass distribution asymmetry in the coordinate system.

$$
\begin{aligned} 
I_{xy} = I_{yx} &= -\int_V \rho_\text{mass} \cdot x y \ dV \\
I_{xz} = I_{zx} &= -\int_V \rho_\text{mass} \cdot  x z \ dV \\
I_{yz} = I_{zy} &= -\int_V \rho_\text{mass} \cdot  y z \ dV 
\end{aligned}
$$

Where:

- $I_{xy} = I_{yx} :=$ [kg·m²] product of inertia for x-y plane: `xy_product_inertia`
- $I_{xz} = I_{zx} :=$ [kg·m²] product of inertia for x-z plane: `xz_product_inertia`
- $I_{yz} = I_{zy} :=$ [kg·m²] product of inertia for y-z plane: `yz_product_inertia`
- $\rho_\text{mass} :=$ [kg/m³] mass density at position (x, y, z) in Body CG frame
- $x, y, z :=$ [meters] coordinates in Body CG frame
- $V :=$ [meters³] volume of the object

___

### D.6 Propulsion

This section defines relationships between propulsion force components and derived thrust quantities.

#### D.6.1 Thrust Relationship

The thrust magnitude represents the total propulsion force applied to the vehicle, calculated from the vector magnitude of the three body-axis force components. The propulsion force vector components represent the actual forces applied to the vehicle in the body frame, accounting for all environmental conditions.

The `Trajectory` schema separately records `thrust_vacuum`, which represents thrust magnitude under vacuum conditions. The vacuum thrust may differ from the actual thrust magnitude due to atmospheric pressure effects on rocket nozzle performance.
$$
\begin{aligned}
\vec{F}_{\text{propulsion}} &= [F_{x,\text{propulsion}}, F_{y,\text{propulsion}}, F_{z,\text{propulsion}}] \\ \\
\text{Thrust} = \|\vec{F}_{\text{propulsion}}\| &= \sqrt{F_{x,\text{propulsion}}^2 + F_{y,\text{propulsion}}^2 + F_{z,\text{propulsion}}^2}
\end{aligned}
$$
Where:

- $\vec{F}_{\text{propulsion}} := $ [newtons] propulsion force vector in Body frame
- $\text{Thrust} := $ [newtons] magnitude of the total propulsion force
- $F_{x,\text{propulsion}} := $ [newtons] propulsion force along body x-axis: `x_force_propulsion`
- $F_{y,\text{propulsion}} := $ [newtons] propulsion force along body y-axis: `y_force_propulsion`
- $F_{z,\text{propulsion}} :=$ [newtons] propulsion force along body z-axis: `z_force_propulsion`

___

### D.7 Geodesy

This section defines geodetic calculations and coordinate system parameters required for Earth-referenced coordinate transformations.

#### D.7.1 Ground Range

[Vincenty's formula](reference/docs/Vincenty-Formula.pdf) is the current standard method for determining ground range between two points on the ellipsoid.

##### D.7.1.1 Point-to-Point Ground Range

Vincenty's formula calculates the geodesic distance between any two geodetic positions (latitude, longitude, altitude). This represents the shortest path along the ellipsoid surface between those points.

##### D.7.1.2 Ground Range Traveled

The cumulative ground range traveled along a trajectory requires numerical integration. At each timestep, calculate the ground range between consecutive trajectory positions using Vincenty's formula, then sum these incremental distances:
$$
\text{Ground Range Traveled}(t_n) = \sum_{i=1}^{n} \text{Ground Range}(\text{LLA}_{i-1}, \text{LLA}_i)
$$
Where:

- $\text{LLA}_i := $ geodetic position (latitude, longitude, altitude) at trajectory index $i$
- $\text{Ground Range}(\text{LLA}_a, \text{LLA}_b) := $ [meters] geodesic distance between two positions calculated using Vincenty's formula

>  **Important Distinction:** The ground range traveled from launch to a given point may significantly exceed the direct point-to-point ground range between launch and that point, particularly for trajectories with lateral maneuvering, non-ballistic flight paths, or orbital trajectories. The point-to-point measurement represents straight-line geodesic distance, while the traveled measurement accounts for the actual path flown.

#### D.7.2 Prime Vertical Radius

The prime vertical radius represents the radius of curvature in the plane perpendicular to the meridian at a given geodetic latitude. This value varies with latitude due to Earth's ellipsoidal shape.
$$
r_{\text{pv}} = \frac{r_a}{\sqrt{1 - \varepsilon^2 \sin^2{\text{(Lat)}}}}
$$

Where:

- $r_{\text{pv}} :=$ [meters] prime vertical radius at reference latitude
- $r_a :=$ [meters] Earth semi-major axis (from [Earth model](#4.1 Earth Shape Models))
- $\varepsilon^2 :=$ first eccentricity squared (from [Earth model](#4.1 Earth Shape Models))
- $\text{Lat} :=$ [radians] geodetic latitude

#### D.7.3 Geoid Correction Term

The geoid correction term accounts for the difference between the geocentric and geodetic vertical references due to Earth's ellipsoidal shape.

$$
z_{\text{geoid}} = \varepsilon^2 \cdot r_{\text{pv}} \cdot \sin{\text{(Lat)}}
$$

Where:

- $z_{\text{geoid}} :=$ [meters] geoid correction term
- $\varepsilon^2 :=$ first eccentricity squared (from [Earth model](#4.1 Earth Shape Models))
- $r_{\text{pv}} :=$ [meters] [prime vertical radius](#d72-prime-vertical-radius)
- $\text{Lat} :=$ [radians] geodetic latitude

---

### D.8 Basic Unit Conversions

This section provides standard unit conversions used throughout trajectory calculations for completeness.

#### D.8.1 Radians to Degrees

Angle conversion from radians to degrees.
$$
\theta_{\text{degrees}} = \theta_{\text{radians}} \times \frac{180°}{\pi}
$$

Where:

- $\theta_{\text{degrees}} :=$ [degrees] angle value
- $\theta_{\text{radians}} :=$ [radians] angle value
- $\pi :=$ mathematical constant pi

#### D.8.2 Degrees to Radians

Angle conversion from degrees to radians.
$$
\theta_{\text{radians}} = \theta_{\text{degrees}} \times \frac{\pi}{180°}
$$

Where:

- $\theta_{\text{radians}} :=$ [radians] angle value
- $\theta_{\text{degrees}} :=$ [degrees] angle value
- $\pi :=$ mathematical constant pi

#### D.8.3 Meters to Kilometers

Distance conversion from meters to kilometers.
$$
d_{\text{kilometers}} = \frac{d_{\text{meters}}}{1000}
$$

Where:

- $d_{\text{kilometers}} :=$ [kilometers] distance
- $d_{\text{meters}} :=$ [meters] distance
