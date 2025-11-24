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
