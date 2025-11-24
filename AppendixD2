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

